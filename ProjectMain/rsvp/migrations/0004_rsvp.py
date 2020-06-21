# Generated by Django 3.0.7 on 2020-06-21 05:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0003_delete_rsvp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rsvp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(max_length=100)),
                ('firsname', models.CharField(max_length=100)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('email', models.EmailField(max_length=100)),
                ('number_guests', models.CharField(max_length=2)),
                ('couple_message', models.TextField()),
            ],
        ),
    ]