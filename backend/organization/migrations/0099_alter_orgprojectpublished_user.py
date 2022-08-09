# Generated by Django 3.2.14 on 2022-08-08 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organization', '0098_orgprojectpublished_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgprojectpublished',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiving_organization_follower', to=settings.AUTH_USER_MODEL, verbose_name='Organization Follower that will receive notification'),
        ),
    ]
