# Generated by Django 4.0.6 on 2022-12-02 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resumes', models.FileField(upload_to='image/pdf')),
            ],
        ),
    ]
