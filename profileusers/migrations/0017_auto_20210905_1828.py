# Generated by Django 3.2.4 on 2021-09-05 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profileusers', '0016_auto_20210905_1813'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profileuser',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='profileuser',
            old_name='last_name',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='profileuser',
            old_name='username',
            new_name='user',
        ),
    ]
