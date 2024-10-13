from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50, unique=True)
    auther = models.CharField(max_length=30)
    year_published = models.PositiveIntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} --- {self.auther}"
