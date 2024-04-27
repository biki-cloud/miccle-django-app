# Generated by Django 5.0.4 on 2024-04-27 06:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('date', models.DateField(default='2019-01-01')),
                ('location', models.CharField(default='default location', max_length=200)),
                ('description', models.TextField(default='default description')),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.organizerprofile')),
            ],
        ),
    ]
