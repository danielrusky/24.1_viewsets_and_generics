# Generated by Django 4.2.10 on 2024-02-18 13:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_payment"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[("member", "member"), ("moderator", "moderator")],
                default="member",
                max_length=20,
                verbose_name="роль",
            ),
        ),
    ]
