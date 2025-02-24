from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=125)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=125, unique=True)
    password = models.CharField(max_length=255)
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
