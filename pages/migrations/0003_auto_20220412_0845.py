# Generated by Django 3.0.7 on 2022-04-12 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20220411_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d'),
        ),
    ]