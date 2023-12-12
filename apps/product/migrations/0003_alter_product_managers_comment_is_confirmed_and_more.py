# Generated by Django 4.2.6 on 2023-11-14 16:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0002_alter_product_managers_product_is_deleted_and_more"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="product",
            managers=[],
        ),
        migrations.AddField(
            model_name="comment",
            name="is_confirmed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="comment",
            name="is_verified_buyer",
            field=models.BooleanField(default=False),
        ),
    ]
