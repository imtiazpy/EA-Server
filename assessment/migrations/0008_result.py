# Generated by Django 4.1.1 on 2022-11-14 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobseekers', '0002_initial'),
        ('assessment', '0007_assessment_is_public'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField(blank=True, null=True, verbose_name='Marks')),
                ('date', models.DateTimeField(auto_now=True)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assessment.assessment')),
                ('job_seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='jobseekers.jobseekersprofile')),
            ],
        ),
    ]