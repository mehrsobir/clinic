from django.db import models


class News(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=100)
    txt = models.TextField()

    def __str__(self):
        return self.title

class DoctorsWorks(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Doctors(models.Model):
    img = models.ImageField()

    name = models.CharField(max_length=100)
    dw = models.ManyToManyField(DoctorsWorks)
    about = models.TextField()
    yw = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Partners(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' - ' + self.city + ', ' + self.country

class Images(models.Model):
    img = models.ImageField()

    def __str__(self):
        return str(self.img)

























