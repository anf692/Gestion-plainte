# Generated by Django 5.1.4 on 2025-03-17 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plainte', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plainte',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
