# Generated by Django 3.2.16 on 2022-11-11 01:50

import arius.fields
from django.db import migrations
import djmoney.models.validators


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_ariussetting'),
        ('company', '0050_alter_company_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplierpricebreak',
            name='price',
            field=arius.fields.AriusModelMoneyField(currency_choices=[], decimal_places=6, default_currency='', help_text='Unit price at specified quantity', max_digits=19, null=True, validators=[djmoney.models.validators.MinMoneyValidator(0)], verbose_name='Price'),
        ),
    ]
