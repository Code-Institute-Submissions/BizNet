# Generated by Django 3.2.4 on 2021-09-05 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profileusers', '0017_auto_20210905_1828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profileuser',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='profileuser',
            old_name='lastname',
            new_name='last_name',
        ),
    ]
