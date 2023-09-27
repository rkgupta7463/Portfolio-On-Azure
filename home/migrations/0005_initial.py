# Generated by Django 4.0.6 on 2022-11-15 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0004_delete_naturaldata'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterestArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='interestImg')),
                ('title', models.CharField(max_length=150)),
                ('descrp', models.TextField()),
            ],
        ),
    ]
