# Generated by Django 3.2.19 on 2023-05-21 13:50

import pint

from django.core.exceptions import ValidationError
from django.db import migrations

import arius.conversion


def migrate_part_units(apps, schema_editor):
    """Update the units field for each Part object:

    - Check if the units are valid
    - Attempt to convert to valid units (if possible)
    """

    Part = apps.get_model('part', 'Part')

    parts = Part.objects.exclude(units=None).exclude(units='')
    n_parts = parts.count()

    if n_parts == 0:
        # Escape early
        return

    ureg = arius.conversion.get_unit_registry()

    invalid_units = set()
    n_converted = 0

    for part in parts:

        # Override '%' units (which are invalid)
        if part.units == '%':
            part.units = 'percent'
            part.save()
            continue

        # Test if unit is 'valid'
        try:
            ureg.Unit(part.units)
            continue
        except Exception:
            pass

        # Check a lower-case version
        try:
            ureg.Unit(part.units.lower())
            print(f"Found unit match: {part.units} -> {part.units.lower()}")
            part.units = part.units.lower()
            part.save()
            n_converted += 1
            continue
        except Exception:
            pass

        found = False

        # Attempt to convert to a valid unit
        for unit in ureg:
            if unit.lower() == part.units.lower():
                print("Found unit match: {part.units} -> {unit}")
                part.units = str(unit)
                part.save()
                n_converted += 1
                found = True
                break

        if not found:
            print(f"Warning: Invalid units for part '{part}': {part.units}")
            invalid_units.add(part.units)

    print(f"Updated units for {n_parts} parts")

    if n_converted > 0:
        print(f"Converted units for {n_converted} parts")

    if len(invalid_units) > 0:
        print(f"Found {len(invalid_units)} invalid units:")
        for unit in invalid_units:
            print(f" - {unit}")


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0110_alter_part_units'),
    ]

    operations = [
        migrations.RunPython(code=migrate_part_units, reverse_code=migrations.RunPython.noop)
    ]
