# Generated by Django 4.0.1 on 2022-02-09 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0026_alter_jobs_comp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobs',
            old_name='date',
            new_name='description',
        ),
    ]