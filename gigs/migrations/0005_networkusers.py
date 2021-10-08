# Generated by Django 3.2.4 on 2021-10-08 20:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profileusers', '0004_termuser'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gigs', '0004_auto_20211004_2106'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(default='profileavatar.png', upload_to='images')),
                ('first_name', models.CharField(max_length=254, null=True)),
                ('last_name', models.CharField(max_length=254, null=True)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=40, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2, null=True)),
                ('title', models.CharField(blank=True, default=None, max_length=254, null=True)),
                ('company_name', models.CharField(blank=True, max_length=254, null=True)),
                ('description', models.TextField(max_length=250, null=True, verbose_name='Description')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('employment', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profileusers.employment')),
                ('follow', models.ManyToManyField(blank=True, related_name='follow', to=settings.AUTH_USER_MODEL)),
                ('gig', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='gigs.gig')),
                ('industry', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profileusers.industry')),
                ('profession', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profileusers.profession')),
                ('status', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profileusers.status')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]