from django.db import models

# Create your models here.
class Category(models.TextChoices):
    WORK = 'Work'
    PERSONAL = 'Personal'
    IDEAS = 'Ideas'

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=25, choices=Category.choices)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
        