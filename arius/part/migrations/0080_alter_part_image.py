# Generated by Django 3.2.13 on 2022-06-27 23:08

from django.db import migrations
import part.models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0079_alter_part_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='image',
            field=stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to=part.models.rename_part_image, variations={'preview': (256, 256), 'thumbnail': (128, 128)}, verbose_name='Image'),
        ),
    ]
