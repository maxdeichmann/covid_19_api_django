# Generated by Django 2.2.11 on 2020-03-18 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200318_0055'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='day',
            unique_together={('date', 'country')},
        ),
    ]
