# Generated by Django 5.1 on 2024-08-16 15:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("weatherapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="temperature",
            name="latitude",
        ),
        migrations.RemoveField(
            model_name="temperature",
            name="longitude",
        ),
        migrations.AddField(
            model_name="city",
            name="latitude",
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="city",
            name="longitude",
            field=models.CharField(blank=True, null=True),
        ),
    ]
