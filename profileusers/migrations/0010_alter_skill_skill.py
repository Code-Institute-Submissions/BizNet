# Generated by Django 3.2.4 on 2021-08-31 12:40

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profileusers', '0009_auto_20210831_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='skill',
            field=multiselectfield.db.fields.MultiSelectField(max_length=100, null=True),
        ),
    ]