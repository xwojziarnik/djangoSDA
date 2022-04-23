from django.db import models


class BookAuthor(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.TextField()
    authors = models.ManyToManyField(BookAuthor)
    publisher = models.TextField(null=True)
    published_date = models.DateField(null=True)
    categories = models.ManyToManyField(Category)
    average_rating = models.FloatField(null=True)

    def __str__(self):
        return f"{self.title} - {self.authors} - {self.published_date}"