# Generated by Django 2.2.13 on 2020-12-21 12:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("organization", "0057_organization_rating"),
        ("hubs", "0004_auto_20201221_0844"),
    ]

    operations = [
        migrations.AddField(
            model_name="hub",
            name="filter_parent_tags",
            field=models.ManyToManyField(
                blank=True,
                help_text="Only project with these parent tags will be shown in the hub",
                related_name="hub_parent_tags",
                to="organization.ProjectTags",
                verbose_name="Hub categories",
            ),
        ),
    ]
