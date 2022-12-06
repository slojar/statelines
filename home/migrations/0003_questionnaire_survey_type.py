# Generated by Django 4.1.3 on 2022-12-06 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_questionnaire_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='survey_type',
            field=models.CharField(choices=[('sender', 'Sender'), ('courier', 'Courier')], default='sender', max_length=100),
        ),
    ]