# Generated by Django 4.0.6 on 2023-01-03 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deshboard', '0002_remove_userimg_profile_image_userimg_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimg',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='media/profile_img'),
        ),
    ]
