# Generated by Django 3.2.4 on 2021-07-09 15:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gigs', '0003_auto_20210708_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gig',
            name='liked',
            field=models.ManyToManyField(blank=True, default=None, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='gig',
            name='picture',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
