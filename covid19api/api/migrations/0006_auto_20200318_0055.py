# Generated by Django 2.2.11 on 2020-03-18 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200318_0040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='total_cases',
        ),
        migrations.RemoveField(
            model_name='country',
            name='total_deaths',
        ),
    ]
