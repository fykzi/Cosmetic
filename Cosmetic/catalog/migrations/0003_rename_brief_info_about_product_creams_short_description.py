# Generated by Django 4.2 on 2023-04-18 20:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0002_creams_brief_info_about_product_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="creams",
            old_name="brief_info_about_product",
            new_name="short_description",
        ),
    ]
