# Generated by Django 2.2.24 on 2021-10-27 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0086_projectlike'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmember',
            name='project',
            field=models.ForeignKey(help_text='Points to project table', on_delete=django.db.models.deletion.CASCADE, related_name='project_member_project', to='organization.Project', verbose_name='Project'),
        ),
        migrations.AlterField(
            model_name='projectmember',
            name='role',
            field=models.ForeignKey(help_text='Points to user role', on_delete=django.db.models.deletion.PROTECT, related_name='project_member_role', to='climateconnect_api.Role', verbose_name='Role(permissions)'),
        ),
        migrations.AlterField(
            model_name='projectmember',
            name='user',
            field=models.ForeignKey(help_text='Points to user table', on_delete=django.db.models.deletion.CASCADE, related_name='project_member_user', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
