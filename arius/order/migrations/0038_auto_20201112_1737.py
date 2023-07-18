# Generated by Django 3.0.7 on 2020-11-12 06:37

from django.db import migrations
import djmoney.models.fields
import common.settings


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_ariussetting'),
        ('order', '0037_auto_20201110_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorderlineitem',
            name='purchase_price',
            field=djmoney.models.fields.MoneyField(decimal_places=4, default_currency=common.settings.currency_code_default(), help_text='Unit purchase price', max_digits=19, null=True, verbose_name='Purchase Price'),
        ),
        migrations.AddField(
            model_name='purchaseorderlineitem',
            name='purchase_price_currency',
            field=djmoney.models.fields.CurrencyField(choices=common.settings.currency_code_mappings(), default=common.settings.currency_code_default(), editable=False, max_length=3),
        ),
    ]
