# Generated by Django 4.0.1 on 2022-02-07 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0005_alter_jobs_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='iscomp',
            field=models.BooleanField(default='false'),
        ),
    ]
