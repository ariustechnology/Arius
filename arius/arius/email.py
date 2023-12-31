"""Code for managing email functionality in arius."""

import logging

from django.conf import settings
from django.core import mail as django_mail

import arius.ready
import arius.tasks

logger = logging.getLogger('arius')


def is_email_configured():
    """Check if email backend is configured.

    NOTE: This does not check if the configuration is valid!
    """
    configured = True

    if arius.ready.isInTestMode():
        return False

    if arius.ready.isImportingData():
        return False

    if not settings.EMAIL_HOST:
        configured = False

        # Display warning unless in test mode
        if not settings.TESTING:  # pragma: no cover
            logger.debug("EMAIL_HOST is not configured")

    # Display warning unless in test mode
    if not settings.EMAIL_HOST_USER and not settings.TESTING:  # pragma: no cover
        logger.debug("EMAIL_HOST_USER is not configured")

    # Display warning unless in test mode
    if not settings.EMAIL_HOST_PASSWORD and not settings.TESTING:  # pragma: no cover
        logger.debug("EMAIL_HOST_PASSWORD is not configured")

    return configured


def send_email(subject, body, recipients, from_email=None, html_message=None):
    """Send an email with the specified subject and body, to the specified recipients list."""

    if type(recipients) == str:
        recipients = [recipients]

    import arius.ready
    import arius.status

    if arius.ready.isImportingData():
        # If we are importing data, don't send emails
        return

    if not arius.email.is_email_configured() and not settings.TESTING:
        # Email is not configured / enabled
        return

    # If a *from_email* is not specified, ensure that the default is set
    if not from_email:
        from_email = settings.DEFAULT_FROM_EMAIL

        # If we still don't have a valid from_email, then we can't send emails
        if not from_email:
            if settings.TESTING:
                from_email = 'from@test.com'
            else:
                logger.error("send_email failed: DEFAULT_FROM_EMAIL not specified")
                return

    arius.tasks.offload_task(
        django_mail.send_mail,
        subject,
        body,
        from_email,
        recipients,
        fail_silently=False,
        html_message=html_message
    )
