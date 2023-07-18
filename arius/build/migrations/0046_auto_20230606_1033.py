# Generated by Django 3.2.19 on 2023-06-06 10:33

import logging

from django.db import migrations


logger = logging.getLogger('arius')


def add_build_line_links(apps, schema_editor):
    """Data migration to add links between BuildLine and BuildItem objects.

    Associated model types:
        Build: A "Build Order"
        BomItem: An individual line in the BOM for Build.part
        BuildItem: An individual stock allocation against the Build Order
        BuildLine: (new model) an individual line in the Build Order

    Goals:
        - Find all BuildItem objects which are associated with a Build
        - Link them against the relevant BuildLine object
        - The BuildLine objects should have been created in 0044_auto_20230528_1410.py
    """

    BuildItem = apps.get_model("build", "BuildItem")
    BuildLine = apps.get_model("build", "BuildLine")

    # Find any existing BuildItem objects
    build_items = BuildItem.objects.all()

    n_missing = 0

    for item in build_items:

        # Find the relevant BuildLine object
        line = BuildLine.objects.filter(
            build=item.build,
            bom_item=item.bom_item
        ).first()

        if line is None:
            logger.warning(f"BuildLine does not exist for BuildItem {item.pk}")
            n_missing += 1

            if item.build is None or item.bom_item is None:
                continue

            # Create one!
            line = BuildLine.objects.create(
                build=item.build,
                bom_item=item.bom_item,
                quantity=item.bom_item.quantity * item.build.quantity
            )

        # Link the BuildItem to the BuildLine
        # In the next data migration, we remove the 'build' and 'bom_item' fields from BuildItem
        item.build_line = line
        item.save()

    if build_items.count() > 0:
        logger.info(f"add_build_line_links: Updated {build_items.count()} BuildItem objects (added {n_missing})")


def reverse_build_links(apps, schema_editor):
    """Reverse data migration from add_build_line_links

    Basically, iterate through each BuildItem and update the links based on the BuildLine
    """

    BuildItem = apps.get_model("build", "BuildItem")

    items = BuildItem.objects.all()

    for item in items:
        item.build = item.build_line.build
        item.bom_item = item.build_line.bom_item
        item.save()

    if items.count() > 0:
        logger.info(f"reverse_build_links: Updated {items.count()} BuildItem objects")


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0045_builditem_build_line'),
    ]

    operations = [
        migrations.RunPython(
            add_build_line_links,
            reverse_code=reverse_build_links,
        )
    ]
