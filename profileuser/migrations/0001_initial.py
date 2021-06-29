# Generated by Django 3.2.4 on 2021-06-29 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id_prof', models.CharField(max_length=254)),
                ('prof_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'Industries',
            },
        ),
        migrations.CreateModel(
            name='Profileuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(blank=True, max_length=254, null=True)),
                ('firstname', models.CharField(max_length=254)),
                ('lastname', models.CharField(max_length=254)),
                ('title', models.CharField(blank=True, max_length=254)),
                ('company_name', models.CharField(max_length=254)),
                ('company_number_vat', models.CharField(blank=True, max_length=254)),
                ('profession', models.CharField(max_length=254)),
                ('skill', models.CharField(max_length=254)),
                ('description', models.TextField(blank=True)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, default='profile-img.jpg', null=True, upload_to='')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('city', models.CharField(max_length=40, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2, null=True)),
                ('industry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profileuser.industry')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]