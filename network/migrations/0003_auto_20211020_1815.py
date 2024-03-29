# Generated by Django 3.2.4 on 2021-10-20 18:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0002_auto_20211019_0757'),
        ('gigs', '0006_delete_networkusers'),
        ('profileusers', '0007_alter_profileuser_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('network', '0002_delete_networkusers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.IntegerField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('user_has_seen', models.BooleanField(default=False)),
                ('notice_locations', django_countries.fields.CountryField(max_length=2, null=True)),
                ('allowed_membership', models.ManyToManyField(to='membership.Membership')),
                ('from_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification_from', to=settings.AUTH_USER_MODEL)),
                ('gig_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='gigs.gig')),
                ('liked', models.ManyToManyField(default=None, to=settings.AUTH_USER_MODEL)),
                ('notice_business', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profileusers.business')),
                ('notice_employment', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profileusers.employment')),
                ('notice_following', models.ManyToManyField(blank=True, related_name='notice_following', to=settings.AUTH_USER_MODEL)),
                ('notice_profession', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profileusers.profession')),
                ('notice_status', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profileusers.status')),
                ('to_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Business',
        ),
        migrations.DeleteModel(
            name='Employment',
        ),
        migrations.DeleteModel(
            name='Industry',
        ),
        migrations.DeleteModel(
            name='Profession',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
