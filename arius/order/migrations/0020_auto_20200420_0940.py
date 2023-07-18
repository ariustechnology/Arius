# Generated by Django 3.0.5 on 2020-04-20 09:40

import arius.fields
import arius.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0021_remove_supplierpart_manufacturer_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0019_purchaseorder_supplier_reference'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(help_text='Order reference', max_length=64, unique=True)),
                ('description', models.CharField(help_text='Order description', max_length=250)),
                ('link', models.URLField(blank=True, help_text='Link to external page')),
                ('creation_date', models.DateField(blank=True, null=True)),
                ('status', models.PositiveIntegerField(choices=[(10, 'Pending'), (20, 'Placed'), (30, 'Complete'), (40, 'Cancelled'), (50, 'Lost'), (60, 'Returned')], default=10, help_text='Order status')),
                ('issue_date', models.DateField(blank=True, null=True)),
                ('complete_date', models.DateField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, help_text='Order notes')),
                ('customer_reference', models.CharField(blank=True, help_text='Customer order reference code', max_length=64)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(help_text='Customer', limit_choices_to={True, 'is_supplier'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales_orders', to='company.Company')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='supplier',
            field=models.ForeignKey(help_text='Supplier', limit_choices_to={'is_supplier': True}, on_delete=django.db.models.deletion.CASCADE, related_name='purchase_orders', to='company.Company'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='supplier_reference',
            field=models.CharField(blank=True, help_text='Supplier order reference code', max_length=64),
        ),
        migrations.CreateModel(
            name='SalesOrderLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', arius.fields.RoundingDecimalField(decimal_places=5, default=1, help_text='Item quantity', max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('reference', models.CharField(blank=True, help_text='Line item reference', max_length=100)),
                ('notes', models.CharField(blank=True, help_text='Line item notes', max_length=500)),
                ('order', models.ForeignKey(help_text='Sales Order', on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='order.SalesOrder')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SalesOrderAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.FileField(help_text='Select file to attach', upload_to=arius.models.rename_attachment)),
                ('comment', models.CharField(help_text='File comment', max_length=100)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='order.SalesOrder')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
