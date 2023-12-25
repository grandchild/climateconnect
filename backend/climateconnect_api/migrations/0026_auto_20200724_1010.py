# Generated by Django 2.2.13 on 2020-07-24 10:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("climateconnect_api", "0025_userprofile_website"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="website",
            field=models.CharField(
                blank=True,
                help_text="Website",
                max_length=256,
                null=True,
                verbose_name="User's Website",
            ),
        ),
    ]
