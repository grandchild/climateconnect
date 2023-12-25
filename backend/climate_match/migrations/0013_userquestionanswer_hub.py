# Generated by Django 2.2.24 on 2021-11-21 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("hubs", "0011_auto_20210505_2011"),
        ("climate_match", "0012_auto_20211121_1949"),
    ]

    operations = [
        migrations.AddField(
            model_name="userquestionanswer",
            name="hub",
            field=models.ForeignKey(
                blank=True,
                help_text="Shows from which (location) hub the user came to the ClimateMatch",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_question_answer_locatin_hub",
                to="hubs.Hub",
                verbose_name="Hub",
            ),
        ),
    ]
