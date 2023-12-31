"""Provides system status functionality checks."""
# -*- coding: utf-8 -*-

import logging
from datetime import timedelta

from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django_q.models import Success
from django_q.monitor import Stat

import arius.email
import arius.ready

logger = logging.getLogger("arius")


def is_worker_running(**kwargs):
    """Return True if the background worker process is oprational."""
    clusters = Stat.get_all()

    if len(clusters) > 0:
        # TODO - Introspect on any cluster information
        return True

    """
    Sometimes Stat.get_all() returns [].
    In this case we have the 'heartbeat' task running every 5 minutes.
    Check to see if we have any successful result within the last 10 minutes
    """

    now = timezone.now()
    past = now - timedelta(minutes=10)

    results = Success.objects.filter(
        started__gte=past
    )

    # If any results are returned, then the background worker is running!
    try:
        result = results.exists()
    except Exception:
        # We may throw an exception if the database is not ready,
        # or if the django_q table is not yet created (i.e. in CI testing)
        result = False

    return result


def check_system_health(**kwargs):
    """Check that the arius system is running OK.

    Returns True if all system checks pass.
    """
    result = True

    if arius.ready.isInTestMode():
        # Do not perform further checks if we are running unit tests
        return False

    if arius.ready.isImportingData():
        # Do not perform further checks if we are importing data
        return False

    if not is_worker_running(**kwargs):  # pragma: no cover
        result = False
        logger.warning(_("Background worker check failed"))

    if not arius.email.is_email_configured():  # pragma: no cover
        result = False
        logger.warning(_("Email backend not configured"))

    if not result:  # pragma: no cover
        logger.warning(_("arius system health checks failed"))

    return result
