from django.db import models


# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=64)
    year = models.IntegerField()
    directory = models.ForeignKey('Person', on_delete=models.CASCADE, null=True)
    category = models.ManyToManyField('Category')

    def __str__(self):
        return f"{self.title} {self.year}"

class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name}"
