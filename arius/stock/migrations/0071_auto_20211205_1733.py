# Generated by Django 3.2.5 on 2021-12-05 06:33

from django.db import migrations

import logging


logger = logging.getLogger('arius')


def delete_scheduled(apps, schema_editor):
    """
    Delete all stock items which are marked as 'scheduled_for_deletion'.

    The issue that this field was addressing has now been fixed,
    and so we can all move on with our lives...
    """

    StockItem = apps.get_model('stock', 'stockitem')

    items = StockItem.objects.filter(scheduled_for_deletion=True)

    if items.count() > 0:
        logger.info(f"Removing {items.count()} stock items scheduled for deletion")

        # Ensure any parent / child relationships are updated!
        for item in items:
            children = StockItem.objects.filter(parent=item)
            children.update(parent=item.parent)

            item.delete()

    Task = apps.get_model('django_q', 'schedule')

    Task.objects.filter(func='stock.tasks.delete_old_stock_items').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('django_q', '0007_ormq'),
        ('stock', '0070_auto_20211128_0151'),
    ]

    operations = [
        migrations.RunPython(
            delete_scheduled,
            reverse_code=migrations.RunPython.noop,
        )
    ]
