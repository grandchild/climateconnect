# Generated by Django 2.2.13 on 2021-01-04 10:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hubs", "0006_hub_stat_box_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="hub",
            name="image_attribution",
            field=models.CharField(
                blank=True,
                help_text="This is incase we have to attribute somebody or a website for using their image",
                max_length=1024,
                null=True,
                verbose_name="Image attribution",
            ),
        ),
    ]
