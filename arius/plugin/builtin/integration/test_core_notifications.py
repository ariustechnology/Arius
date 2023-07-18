"""Tests for core_notifications."""

from django.core import mail

from part.test_part import BaseNotificationIntegrationTest
from plugin import registry
from plugin.builtin.integration.core_notifications import \
    AriusCoreNotificationsPlugin
from plugin.models import NotificationUserSetting


class CoreNotificationTestTests(BaseNotificationIntegrationTest):
    """Tests for CoreNotificationsPlugin."""

    def test_email(self):
        """Ensure that the email notifications run."""
        # No email should be send
        self.assertEqual(len(mail.outbox), 0)

        # enable plugin and set mail setting to true
        plugin = registry.plugins.get('ariuscorenotificationsplugin')
        plugin.set_setting('ENABLE_NOTIFICATION_EMAILS', True)
        NotificationUserSetting.set_setting(
            key='NOTIFICATION_METHOD_MAIL',
            value=True,
            change_user=self.user,
            user=self.user,
            method=AriusCoreNotificationsPlugin.EmailNotification.METHOD_NAME
        )

        # run through
        self._notification_run(AriusCoreNotificationsPlugin.EmailNotification)

        # Now one mail should be send
        self.assertEqual(len(mail.outbox), 1)
