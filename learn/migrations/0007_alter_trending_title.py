# Generated by Django 4.0.6 on 2022-12-10 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0006_trending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trending',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
