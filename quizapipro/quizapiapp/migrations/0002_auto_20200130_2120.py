# Generated by Django 2.0.1 on 2020-01-30 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizapiapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='eno',
            new_name='emp_id',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='eaddr',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='ename',
            new_name='lastname',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='esal',
        ),
    ]
