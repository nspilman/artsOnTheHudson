# Generated by Django 2.2 on 2019-04-23 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='bullshit',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bullshit',
        ),
    ]