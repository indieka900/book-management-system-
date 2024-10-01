from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50, unique=True)
    auther = models.CharField(max_length=30)
    year_published = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.title} --- {self.auther}"
