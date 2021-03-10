# Generated by Django 2.2.19 on 2021-03-09 18:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('oficinas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=255)),
                ('user_create_reserve', models.CharField(max_length=255)),
                ('date_reserve', models.DateTimeField(default=datetime.date.today)),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserve', to='oficinas.Office')),
            ],
        ),
    ]