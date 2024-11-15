# Generated by Django 4.2.16 on 2024-11-09 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_alter_habit_description_alter_habit_plan_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="todo",
            name="subTasks",
        ),
        migrations.CreateModel(
            name="SubTodo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=128)),
                ("estimatedDuration", models.IntegerField(null=True)),
                ("duration", models.IntegerField(null=True)),
                ("completed", models.BooleanField(default=False)),
                (
                    "todo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.todo"
                    ),
                ),
            ],
        ),
    ]
