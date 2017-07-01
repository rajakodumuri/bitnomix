from django.db import models

import datetime
from django.utils import timezone

# Create your models here.
class Categories(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length = 50, default = "Unknown")

    def __str__(self):
        return self.name

class Authors(models.Model):
    class Meta:
        verbose_name_plural = "Authors"

    name = models.CharField(max_length = 50, default = "Unknown")
    bio = models.TextField(max_length = 1000, default = "Unknown")
    email = models.EmailField(max_length = 60, default = "unknown@email.com")

    def __str__(self):
        return self.name

class Books(models.Model):
    class Meta:
        verbose_name_plural = "Books"

    name = models.CharField(max_length = 50, default = "Unknown")
    pubdate = models.DateTimeField('date published')
    author = models.ForeignKey(Authors, on_delete = models.CASCADE)
    category = models.ForeignKey(Categories, on_delete = models.CASCADE)

    def __str__(self):
        return self.name
