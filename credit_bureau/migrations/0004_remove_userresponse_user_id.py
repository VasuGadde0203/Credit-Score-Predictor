# Generated by Django 5.1.2 on 2024-11-13 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("credit_bureau", "0003_remove_question_correct_answer"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userresponse",
            name="user_id",
        ),
    ]
