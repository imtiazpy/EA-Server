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
            name='TrueFalseQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(help_text='Enter you question', max_length=1000, verbose_name='Content')),
                ('is_true', models.BooleanField(default=False, help_text='Is This True?', verbose_name='Is True')),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tf_questions', to='assessment.assessment', verbose_name='Assessment')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assessment.questiontopic', verbose_name='Topic')),
            ],
            options={
                'verbose_name': 'True False Question',
                'verbose_name_plural': 'True False Questions',
                'ordering': ['topic'],
            },
        ),
    ]
