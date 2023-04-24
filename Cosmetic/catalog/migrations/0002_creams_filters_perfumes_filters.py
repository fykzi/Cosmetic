# Generated by Django 4.2 on 2023-04-24 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="creams",
            name="filters",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="catalog.modelfilters",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="perfumes",
            name="filters",
            field=models.ForeignKey(
                default=5443,
                on_delete=django.db.models.deletion.CASCADE,
                to="catalog.modelfilters",
            ),
            preserve_default=False,
        ),
    ]
