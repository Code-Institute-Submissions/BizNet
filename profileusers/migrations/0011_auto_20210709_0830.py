# Generated by Django 3.2.4 on 2021-07-09 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileusers', '0010_auto_20210709_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='avatar',
            field=models.ImageField(default='profileavatars/profileavatar.png', upload_to='profileavatars'),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='background',
            field=models.ImageField(default='backgroundpics/backgroundpic.jpg', upload_to='backgroundpics'),
        ),
    ]
