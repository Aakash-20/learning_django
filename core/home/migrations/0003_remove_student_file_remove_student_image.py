# Generated by Django 5.1.1 on 2024-10-01 10:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_alter_student_address"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="file",
        ),
        migrations.RemoveField(
            model_name="student",
            name="image",
        ),
    ]
