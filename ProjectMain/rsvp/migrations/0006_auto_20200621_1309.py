# Generated by Django 3.0.7 on 2020-06-21 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0005_auto_20200621_1059'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Responses',
            new_name='Response',
        ),
    ]