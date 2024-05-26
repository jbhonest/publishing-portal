from django.db import models
from django.core.exceptions import ValidationError


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    headshot = models.ImageField(
        upload_to="author_headshots", null=True, blank=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField("Author")
    cover = models.ImageField(upload_to="book_covers", null=True, blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT)
    publication_date = models.DateField()

    class Meta:
        ordering = ["-id"]

    def delete(self):
        # Delete the image file from the storage
        if self.cover:
            storage, path = self.cover.storage, self.cover.path
            storage.delete(path)

        # Call the parent class's delete method to remove the model instance from the database
        super().delete()

    def __str__(self):
        return self.title
