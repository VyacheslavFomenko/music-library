# Generated by Django 5.0.6 on 2024-06-05 17:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="song",
            name="performer",
            field=models.ManyToManyField(
                related_name="performer", to="catalog.performer"
            ),
        ),
        migrations.AlterField(
            model_name="song",
            name="duration",
            field=models.FloatField(),
        ),
    ]
