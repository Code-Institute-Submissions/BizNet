# Generated by Django 3.2.4 on 2021-09-15 06:54

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profileusers', '0019_rename_user_profileuser_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Businesses',
            },
        ),
        migrations.AddField(
            model_name='profileuser',
            name='locations',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='business',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profileusers.business'),
        ),
    ]
