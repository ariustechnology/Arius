# Generated by Django 3.2.19 on 2023-05-19 03:31

import arius.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0109_auto_20230517_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='units',
            field=models.CharField(blank=True, default='', help_text='Units of measure for this part', max_length=20, null=True, validators=[arius.validators.validate_physical_units], verbose_name='Units'),
        ),
    ]