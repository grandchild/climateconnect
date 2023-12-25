# Generated by Django 2.2.24 on 2021-10-27 08:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("climateconnect_api", "0068_auto_20211026_2135"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="email_on_new_project_like",
            field=models.BooleanField(
                blank=True,
                default=True,
                help_text="Check if user wants to receive emails when somebody likes their project",
                null=True,
                verbose_name="Email on new project like",
            ),
        ),
    ]
