# Generated by Django 4.1.6 on 2023-07-15 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_mebel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mebel',
            name='image',
            field=models.ImageField(upload_to='Furnature/%Y/%m/%d'),
        ),
    ]
