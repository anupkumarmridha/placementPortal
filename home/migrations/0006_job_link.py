# Generated by Django 4.1.2 on 2022-10-16 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_alter_job_deadline"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="link",
            field=models.CharField(
                default="https://forms.gle/aMQFV8DkUhmefzvu8", max_length=500
            ),
        ),
    ]