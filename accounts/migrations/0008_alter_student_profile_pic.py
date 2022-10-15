# Generated by Django 4.1.2 on 2022-10-15 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0007_alter_educationdetails_resume_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="profile_pic",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="images/Students/profile/f'{instance.user.user.username}'",
            ),
        ),
    ]
