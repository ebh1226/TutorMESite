# Generated by Django 4.1.7 on 2023-04-17 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "tutorme11",
            "0010_alter_class_catalog_nbr_alter_class_class_section_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="class",
            name="unique_id",
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
    ]
