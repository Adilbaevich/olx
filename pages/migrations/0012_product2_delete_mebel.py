# Generated by Django 4.1.6 on 2023-07-15 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_product1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='products3/%Y/%m/%d/')),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Mebel',
        ),
    ]