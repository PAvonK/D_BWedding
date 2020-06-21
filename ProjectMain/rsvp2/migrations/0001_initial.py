# Generated by Django 3.0.7 on 2020-06-21 05:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rsvp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('email', models.EmailField(max_length=75)),
                ('attending', models.BooleanField()),
                ('number_attending', models.IntegerField()),
                ('message_for_the_happy_couple', models.TextField(blank=True, max_length=500)),
            ],
        ),
    ]