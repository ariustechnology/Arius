# Generated by Django 3.0.7 on 2021-04-04 20:16

import arius.models
import arius.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import part.models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock', '0058_stockitem_packaging'),
        ('part', '0063_bomitem_inherited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bomitem',
            name='checksum',
            field=models.CharField(blank=True, help_text='BOM line checksum', max_length=128, verbose_name='Checksum'),
        ),
        migrations.AlterField(
            model_name='bomitem',
            name='note',
            field=models.CharField(blank=True, help_text='BOM item notes', max_length=500, verbose_name='Note'),
        ),
        migrations.AlterField(
            model_name='bomitem',
            name='optional',
            field=models.BooleanField(default=False, help_text='This BOM item is optional', verbose_name='Optional'),
        ),
        migrations.AlterField(
            model_name='bomitem',
            name='overage',
            field=models.CharField(blank=True, help_text='Estimated build wastage quantity (absolute or percentage)', max_length=24, validators=[arius.validators.validate_overage], verbose_name='Overage'),
        ),
        migrations.AlterField(
            model_name='bomitem',
            name='part',
            field=models.ForeignKey(help_text='Select parent part', limit_choices_to={'assembly': True}, on_delete=django.db.models.deletion.CASCADE, related_name='bom_items', to='part.Part', verbose_name='Part'),
        ),
        migrations.AlterField(
            model_name='bomitem',
            name='quantity',
            field=models.DecimalField(decimal_places=5, default=1.0, help_text='BOM quantity for this BOM item', max_digits=15, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='bomitem',
            name='reference',
            field=models.CharField(blank=True, help_text='BOM item reference', max_length=500, verbose_name='Reference'),
        ),
        migrations.AlterField(
            model_name='bomitem',
            name='sub_part',
            field=models.ForeignKey(help_text='Select part to be used in BOM', limit_choices_to={'component': True}, on_delete=django.db.models.deletion.CASCADE, related_name='used_in', to='part.Part', verbose_name='Sub part'),
        ),
        migrations.AlterField(
            model_name='part',
            name='bom_checked_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='boms_checked', to=settings.AUTH_USER_MODEL, verbose_name='BOM checked by'),
        ),
        migrations.AlterField(
            model_name='part',
            name='bom_checked_date',
            field=models.DateField(blank=True, null=True, verbose_name='BOM checked date'),
        ),
        migrations.AlterField(
            model_name='part',
            name='bom_checksum',
            field=models.CharField(blank=True, help_text='Stored BOM checksum', max_length=128, verbose_name='BOM checksum'),
        ),
        migrations.AlterField(
            model_name='part',
            name='creation_date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Creation Date'),
        ),
        migrations.AlterField(
            model_name='part',
            name='creation_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parts_created', to=settings.AUTH_USER_MODEL, verbose_name='Creation User'),
        ),
        migrations.AlterField(
            model_name='part',
            name='image',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to=part.models.rename_part_image, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='part',
            name='responsible',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parts_responible', to=settings.AUTH_USER_MODEL, verbose_name='Responsible'),
        ),
        migrations.AlterField(
            model_name='partattachment',
            name='attachment',
            field=models.FileField(help_text='Select file to attach', upload_to=arius.models.rename_attachment, verbose_name='Attachment'),
        ),
        migrations.AlterField(
            model_name='partattachment',
            name='comment',
            field=models.CharField(blank=True, help_text='File comment', max_length=100, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='partattachment',
            name='part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='part.Part', verbose_name='Part'),
        ),
        migrations.AlterField(
            model_name='partattachment',
            name='upload_date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='upload date'),
        ),
        migrations.AlterField(
            model_name='partattachment',
            name='user',
            field=models.ForeignKey(blank=True, help_text='User', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='partcategory',
            name='default_keywords',
            field=models.CharField(blank=True, help_text='Default keywords for parts in this category', max_length=250, null=True, verbose_name='Default keywords'),
        ),
        migrations.AlterField(
            model_name='partcategory',
            name='default_location',
            field=mptt.fields.TreeForeignKey(blank=True, help_text='Default location for parts in this category', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='default_categories', to='stock.StockLocation', verbose_name='Default Location'),
        ),
        migrations.AlterField(
            model_name='partcategory',
            name='description',
            field=models.CharField(blank=True, help_text='Description (optional)', max_length=250, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='partcategory',
            name='name',
            field=models.CharField(help_text='Name', max_length=100, validators=[arius.validators.validate_tree_name], verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='partcategory',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='children', to='part.PartCategory', verbose_name='parent'),
        ),
        migrations.AlterField(
            model_name='partcategoryparametertemplate',
            name='category',
            field=models.ForeignKey(help_text='Part Category', on_delete=django.db.models.deletion.CASCADE, related_name='parameter_templates', to='part.PartCategory', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='partcategoryparametertemplate',
            name='default_value',
            field=models.CharField(blank=True, help_text='Default Parameter Value', max_length=500, verbose_name='Default Value'),
        ),
        migrations.AlterField(
            model_name='partcategoryparametertemplate',
            name='parameter_template',
            field=models.ForeignKey(help_text='Parameter Template', on_delete=django.db.models.deletion.CASCADE, related_name='part_categories', to='part.PartParameterTemplate', verbose_name='Parameter Template'),
        ),
        migrations.AlterField(
            model_name='partparameter',
            name='data',
            field=models.CharField(help_text='Parameter Value', max_length=500, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='partparameter',
            name='part',
            field=models.ForeignKey(help_text='Parent Part', on_delete=django.db.models.deletion.CASCADE, related_name='parameters', to='part.Part', verbose_name='Part'),
        ),
        migrations.AlterField(
            model_name='partparameter',
            name='template',
            field=models.ForeignKey(help_text='Parameter Template', on_delete=django.db.models.deletion.CASCADE, related_name='instances', to='part.PartParameterTemplate', verbose_name='Template'),
        ),
        migrations.AlterField(
            model_name='partparametertemplate',
            name='name',
            field=models.CharField(help_text='Parameter Name', max_length=100, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='partparametertemplate',
            name='units',
            field=models.CharField(blank=True, help_text='Parameter Units', max_length=25, verbose_name='Units'),
        ),
        migrations.AlterField(
            model_name='partrelated',
            name='part_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='related_parts_1', to='part.Part', verbose_name='Part 1'),
        ),
        migrations.AlterField(
            model_name='partrelated',
            name='part_2',
            field=models.ForeignKey(help_text='Select Related Part', on_delete=django.db.models.deletion.DO_NOTHING, related_name='related_parts_2', to='part.Part', verbose_name='Part 2'),
        ),
        migrations.AlterField(
            model_name='partsellpricebreak',
            name='part',
            field=models.ForeignKey(limit_choices_to={'salable': True}, on_delete=django.db.models.deletion.CASCADE, related_name='salepricebreaks', to='part.Part', verbose_name='Part'),
        ),
        migrations.AlterField(
            model_name='partstar',
            name='part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='starred_users', to='part.Part', verbose_name='Part'),
        ),
        migrations.AlterField(
            model_name='partstar',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='starred_parts', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='parttesttemplate',
            name='part',
            field=models.ForeignKey(limit_choices_to={'trackable': True}, on_delete=django.db.models.deletion.CASCADE, related_name='test_templates', to='part.Part', verbose_name='Part'),
        ),
    ]
