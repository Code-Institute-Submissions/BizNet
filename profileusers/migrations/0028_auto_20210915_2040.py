# Generated by Django 3.2.4 on 2021-09-15 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profileusers', '0027_auto_20210915_1935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileuser',
            name='employment',
        ),
        migrations.RemoveField(
            model_name='profileuser',
            name='status',
        ),
    ]