# Generated by Django 3.2.8 on 2021-10-13 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventsAPI', '0002_currenttime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='actual_time',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='color',
            field=models.CharField(max_length=30, null=True),
        ),
    ]