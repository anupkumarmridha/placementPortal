# Generated by Django 4.1.2 on 2022-10-15 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_alter_student_class10percentage_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="currentCgpa",
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
