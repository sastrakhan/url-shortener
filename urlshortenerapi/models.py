# models.py
from django.db import models
from .utilities import generate_id_from_url
from django.utils.text import slugify

class URL(models.Model):
    original_name = models.CharField(max_length=100)
    shortened_version = models.CharField(max_length=8)
    latest_custom_url = models.CharField(max_length=50, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.shortened_version

    def save(self, *args, **kwargs):
        self.original_name = slugify(self.original_name)
        self.latest_custom_url = slugify(self.latest_custom_url)
        self.shortened_version = generate_id_from_url(self.original_name)
        super(URL, self).save(*args, **kwargs)

class URLVisit(models.Model):
    date_visited = models.DateTimeField(auto_now_add=True)
    url = models.ForeignKey(URL, on_delete=models.CASCADE)

    def __str__(self):
        return f"self.url{str(self.date_visited)}"

    class Meta:
        ordering = ['date_visited']

class CustomURL(models.Model):
    name = models.CharField(max_length=50)
    parent_url = models.ForeignKey(URL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_date']