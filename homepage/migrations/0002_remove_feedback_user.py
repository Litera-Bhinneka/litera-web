# Generated by Django 4.2.6 on 2023-10-16 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="feedback",
            name="user",
        ),
    ]
