# Generated by Django 2.2.11 on 2020-03-18 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20200318_1004'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='day',
            name='unique_date',
        ),
    ]
