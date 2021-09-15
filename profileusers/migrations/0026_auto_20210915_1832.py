# Generated by Django 3.2.4 on 2021-09-15 18:32

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profileusers', '0025_auto_20210915_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]
