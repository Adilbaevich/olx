from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Product(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/%Y/%m/%d')
    description = models.TextField()
    price = models.PositiveIntegerField()
    author = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse(
            'transport_detail',
            args=[self.pk]
        )


    class Meta:
        ordering = ['-id']

    

class Product1(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products1/%Y/%m/%d')
    description = models.TextField()
    date = models.DateField()
    price = models.PositiveIntegerField()
    
    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-id']

class Product2(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products2/%Y/%m/%d')
    description = models.TextField()
    price = models.PositiveIntegerField()
    author = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'electro_detail',
            args=[self.pk]
        )

    class Meta:
        ordering = ['-id']


class Product3(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products3/%Y/%m/%d')
    description = models.TextField()
    price = models.PositiveIntegerField()
    author = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'animal_detail',
            args=[self.pk]
        )


    class Meta:
        ordering = ['-id']

class Product4(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products4/%Y/%m/%d')
    description = models.TextField()
    date = models.DateField()
    price = models.PositiveIntegerField()
    author = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'furnature_detail',
            args=[self.pk]
        )

    class Meta:
        ordering = ['-id']


