# Generated by Django 3.2.4 on 2021-10-07 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileusers', '0003_delete_termsagree'),
    ]

    operations = [
        migrations.CreateModel(
            name='TermUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agree', models.BooleanField()),
            ],
        ),
    ]
