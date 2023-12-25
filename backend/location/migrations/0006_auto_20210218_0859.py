# Generated by Django 2.2.13 on 2021-02-18 08:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("location", "0005_auto_20210211_1645"),
    ]

    operations = [
        migrations.AlterField(
            model_name="location",
            name="osm_id",
            field=models.BigIntegerField(
                blank=True,
                help_text="The internal id of this location openstreetmaps",
                null=True,
                verbose_name="OSM ID",
            ),
        ),
        migrations.AlterField(
            model_name="location",
            name="place_id",
            field=models.BigIntegerField(
                blank=True,
                help_text="Nominatim's place id of this location",
                null=True,
                verbose_name="Place ID",
            ),
        ),
    ]
