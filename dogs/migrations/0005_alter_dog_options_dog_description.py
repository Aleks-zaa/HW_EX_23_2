# Generated by Django 4.2.2 on 2024-06-26 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dogs", "0004_dog_owner"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="dog",
            options={
                "ordering": ["bread", "name"],
                "permissions": [
                    ("can_edit_bread", "Can edit bread"),
                    ("can_edit_description", "Can edit description"),
                ],
                "verbose_name": "Собака",
                "verbose_name_plural": "Собаки",
            },
        ),
        migrations.AddField(
            model_name="dog",
            name="description",
            field=models.TextField(
                blank=True,
                help_text="Введите описание собаки",
                null=True,
                verbose_name="Описание собаки",
            ),
        ),
    ]
