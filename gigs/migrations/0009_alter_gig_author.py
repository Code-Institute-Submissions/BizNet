# Generated by Django 3.2.4 on 2021-07-10 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profileusers', '0016_alter_profileuser_background'),
        ('gigs', '0008_auto_20210710_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gig',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gig', to='profileusers.profileuser'),
        ),
    ]
