# Generated by Django 4.1.6 on 2023-08-12 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0021_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product3',
            name='author',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product3',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
