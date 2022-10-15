# Generated by Django 4.1.2 on 2022-10-15 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="class10Percentage",
        ),
        migrations.RemoveField(
            model_name="student",
            name="class12Percentage",
        ),
        migrations.RemoveField(
            model_name="student",
            name="collageGraduationYear",
        ),
        migrations.RemoveField(
            model_name="student",
            name="currentCgpa",
        ),
        migrations.RemoveField(
            model_name="student",
            name="currentCourse",
        ),
        migrations.RemoveField(
            model_name="student",
            name="currentCourseGraduationYear",
        ),
        migrations.RemoveField(
            model_name="student",
            name="currentDept",
        ),
        migrations.RemoveField(
            model_name="student",
            name="graduationCgpa",
        ),
        migrations.RemoveField(
            model_name="student",
            name="graduationCollage",
        ),
        migrations.RemoveField(
            model_name="student",
            name="graduationDegree",
        ),
        migrations.RemoveField(
            model_name="student",
            name="resume",
        ),
        migrations.RemoveField(
            model_name="student",
            name="roll",
        ),
        migrations.AlterField(
            model_name="user",
            name="user_type",
            field=models.CharField(
                choices=[(1, "Admin"), (2, "Student")], default=2, max_length=20
            ),
        ),
        migrations.CreateModel(
            name="EducationDetails",
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
                ("roll", models.CharField(max_length=9, unique=True)),
                (
                    "degreeLevel",
                    models.CharField(
                        choices=[("UG", "UG"), ("PG", "PG")], max_length=20
                    ),
                ),
                ("currentDept", models.CharField(max_length=255)),
                ("currentCourse", models.CharField(max_length=255)),
                ("currentCgpa", models.DecimalField(decimal_places=2, max_digits=5)),
                (
                    "currentCourseGraduationYear",
                    models.DateField(blank=True, null=True),
                ),
                (
                    "class10Percentage",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
                (
                    "class12Percentage",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
                ("ugDegree", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "ugCgpa",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                ("ugCollege", models.CharField(blank=True, max_length=500, null=True)),
                ("ugGraduationYear", models.DateField(blank=True, null=True)),
                (
                    "resume",
                    models.FileField(
                        blank=True, null=True, upload_to="PDF/Students/resume/"
                    ),
                ),
                (
                    "student",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.student",
                    ),
                ),
            ],
        ),
    ]
