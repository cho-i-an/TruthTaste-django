# Generated by Django 4.2.6 on 2023-11-01 19:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("truthtaste", "0002_alter_storebox_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="storebox",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="restaurant/"),
        ),
    ]
