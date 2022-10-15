# Generated by Django 4.1.2 on 2022-10-15 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="class10Percentage",
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name="student",
            name="class12Percentage",
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name="student",
            name="graduationCgpa",
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name="student",
            name="graduationCollage",
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
