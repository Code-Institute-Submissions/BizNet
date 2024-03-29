# Generated by Django 3.2.4 on 2021-10-19 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermembership',
            name='cancel_at_period_end',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='membership',
            name='membership_type',
            field=models.CharField(choices=[('Yearly', 'yearly'), ('Monthly', 'monthly'), ('Free', 'free')], default='Free', max_length=30),
        ),
    ]
