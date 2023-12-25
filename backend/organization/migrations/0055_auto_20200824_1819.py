# Generated by Django 2.2.13 on 2020-08-24 18:19

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("organization", "0054_auto_20200819_1619"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="helpful_connections",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=264),
                blank=True,
                null=True,
                size=10,
            ),
        ),
    ]
