# Generated by Django 4.1.5 on 2023-03-05 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0002_alter_resume_resumes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="resume",
            name="resumes",
            field=models.FileField(upload_to="image/pdf"),
        ),
    ]
