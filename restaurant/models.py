from django.db import models

from django.utils import timezone



# Create your models here.

class Homepage(models.Model):
    heading = models.CharField(max_length=500, default='heading')
    description = models.TextField(max_length=3000, default='description')
    text1 = models.CharField(max_length=500, default='text1')
    text2 = models.CharField(max_length=500, default='text2')
    text3 = models.CharField(max_length=500, default='text3')
    btn = models.CharField(max_length=20, default='button')
    background_image1 = models.ImageField(upload_to='homepage', default='homepage.jpg')
    background_image1 = models.ImageField(upload_to='homepage', default='homepage.jpg')

    def __str__(self):
        return self.heading


class Customer(models.Model):
    name = models.CharField(max_length=150, blank=False)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    date = models.CharField(max_length=10, default='dd/mm/yyyy')
    time = models.TimeField(max_length=50, default=timezone.now)
    person = models.IntegerField()

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=50, default='name')
    heading = models.CharField(max_length=50, default='heading')
    #BREAKFAST
    text1 = models.CharField(max_length=500, default='text1')
    text2 = models.CharField(max_length=500, default='text2')
    text3 = models.CharField(max_length=500, default='text3')
    text4 = models.CharField(max_length=500, default='text4')
    text5 = models.CharField(max_length=500, default='text5')
    text6 = models.CharField(max_length=500, default='text6')
    text7 = models.CharField(max_length=500, default='text4')
    text8 = models.CharField(max_length=500, default='text5')
    text9 = models.CharField(max_length=500, default='text6')
    text10 = models.CharField(max_length=500, default='text4')
    text11 = models.CharField(max_length=500, default='text5')
    text12 = models.CharField(max_length=500, default='text6')
    text16 = models.CharField(max_length=500, default='text4')
    text17 = models.CharField(max_length=500, default='text5')
    text18 = models.CharField(max_length=500, default='text6')
    text19 = models.CharField(max_length=500, default='text4')
    text20 = models.CharField(max_length=500, default='text5')
    text21 = models.CharField(max_length=500, default='text6')

    def __str__(self):
        return self.name




class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=100, decimal_places=2)


class Aboutpage(models.Model):
    heading = models.CharField(max_length=500, default='hading')
    welcome = models.CharField(max_length=500, default='welcome')
    description = models.TextField(max_length=3000, default='description')
    special = models.CharField(max_length=500, default='specialmenu')
    text1 = models.CharField(max_length=500, default='text1')
    text2 = models.CharField(max_length=500, default='text2')
    text3 = models.CharField(max_length=500, default='text3')

    def __str__(self):
        return self.heading


class Stories(models.Model):
    text1 = models.TextField(max_length=500, default='text1')
    text2 = models.TextField(max_length=500, default='text2')
    text3 = models.TextField(max_length=500, default='text3')
    text4 = models.TextField(max_length=500, default='text4')
    text5 = models.TextField(max_length=500, default='text5')
    text6 = models.TextField(max_length=500, default='text6')

    def __str__(self):
        return self.text1