# Generated by Django 2.2.11 on 2020-03-17 19:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('total_cases', models.IntegerField()),
                ('total_deaths', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('new_cases', models.IntegerField()),
                ('new_deaths', models.IntegerField()),
                ('total_cases', models.IntegerField()),
                ('total_deaths', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Country')),
            ],
        ),
    ]
