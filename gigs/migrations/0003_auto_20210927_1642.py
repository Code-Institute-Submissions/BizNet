# Generated by Django 3.2.4 on 2021-09-27 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gigs', '0002_auto_20210927_1212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gig',
            old_name='description',
            new_name='overview',
        ),
        migrations.AddField(
            model_name='gig',
            name='position',
            field=models.TextField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='gig',
            name='requirements',
            field=models.TextField(max_length=250, null=True),
        ),
    ]
