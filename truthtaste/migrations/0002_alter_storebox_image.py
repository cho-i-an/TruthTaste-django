# Generated by Django 4.2.6 on 2023-11-01 18:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("truthtaste", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="storebox",
            name="image",
            field=models.ImageField(upload_to="restaurant/"),
        ),
    ]
