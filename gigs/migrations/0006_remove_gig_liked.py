# Generated by Django 3.2.4 on 2021-07-10 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gigs', '0005_alter_gig_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gig',
            name='liked',
        ),
    ]
