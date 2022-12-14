# Generated by Django 4.1.1 on 2022-09-28 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('MCQ', 'mcq'), ('SHORT_ANSWER', 'short_answer'), ('TRUE_FALSE', 'true_false')], max_length=50, verbose_name='Type')),
                ('title', models.CharField(help_text='Title of your Assessment', max_length=100, verbose_name='Title')),
                ('duration', models.DurationField(blank=True, null=True, verbose_name='Duration')),
                ('is_published', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
            ],
        ),
        migrations.CreateModel(
            name='MCQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(help_text='Enter you question', max_length=1000, verbose_name='Content')),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mcquestions', to='assessment.assessment')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='assessment.questiontopic')),
            ],
            options={
                'verbose_name': 'Multiple Choice Question',
                'verbose_name_plural': 'Multiple Choice Questions',
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(help_text='Enter the text that you want displayed as choice', max_length=1000, verbose_name='Content')),
                ('is_correct', models.BooleanField(default=False, help_text='Is this correct answer?', verbose_name='Is Correct')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='assessment.mcquestion', verbose_name='Question')),
            ],
            options={
                'verbose_name': 'Choice',
                'verbose_name_plural': 'Choices',
            },
        ),
    ]
