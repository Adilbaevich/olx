# Generated by Django 4.1.6 on 2023-08-12 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0024_remove_product2_date_product2_author_product2_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='product2',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='product3',
            name='slug',
        ),
        migrations.AddField(
            model_name='product4',
            name='author',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product1',
            name='image',
            field=models.ImageField(upload_to='products1/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product2',
            name='image',
            field=models.ImageField(upload_to='products2/%Y/%m/%d'),
        ),
    ]
