# Generated by Django 3.2.4 on 2021-08-31 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileusers', '0006_auto_20210813_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileuser',
            name='background',
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='skill',
            field=models.CharField(blank=True, default=None, max_length=254, null=True),
        ),
    ]
