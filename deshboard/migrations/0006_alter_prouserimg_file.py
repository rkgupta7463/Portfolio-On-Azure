# Generated by Django 4.0.6 on 2023-01-04 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deshboard', '0005_prouserimg_delete_userimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prouserimg',
            name='file',
            field=models.FileField(blank=True, upload_to='media/profile_img/'),
        ),
    ]
