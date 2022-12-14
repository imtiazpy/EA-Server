# Generated by Django 4.1.1 on 2022-10-05 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assessment', '0005_remove_choice_question_remove_mcquestion_assessment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MCQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(help_text='Enter you question', max_length=1000, verbose_name='Content')),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mc_questions', to='assessment.assessment', verbose_name='Assessment')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assessment.questiontopic', verbose_name='Topic')),
            ],
            options={
                'verbose_name': 'Multiple Choice Question',
                'verbose_name_plural': 'Multiple Choice Questions',
                'ordering': ['topic'],
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(help_text='Enter the text that you want displayed as choice', max_length=1000, verbose_name='Content')),
                ('is_correct', models.BooleanField(default=False, help_text='Is this correct answer?', verbose_name='Is Correct')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='mcq.mcquestion', verbose_name='Question')),
            ],
            options={
                'verbose_name': 'Choice',
                'verbose_name_plural': 'Choices',
            },
        ),
    ]
