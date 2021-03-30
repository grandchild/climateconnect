# Generated by Django 2.2.13 on 2021-03-08 06:18

import climateconnect_api.models.user
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climateconnect_api', '0048_auto_20210305_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='thumbnail_image',
            field=models.ImageField(blank=True, help_text='The small image that shows on the user preview', null=True, upload_to=climateconnect_api.models.user.profile_image_path, verbose_name='Thumbnail Image'),
        ),
    ]