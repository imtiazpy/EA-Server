# Generated by Django 4.1.1 on 2022-09-23 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobseekers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobseekersprofile',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='job_seeker_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
