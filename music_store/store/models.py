from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.utils import timezone

# Validator for album release year
def validate_year(value):
    year = value.year
    current_year = timezone.now().year
    if year < 1800 or year > current_year:
        raise ValidationError(f'Year must be between 1800 and {current_year}')
    
class Artist(models.Model):
    name = models.CharField (max_length=100, validators=[MinLengthValidator(2)])
    debut_year = models.PositiveIntegerField()
    picture = models.ImageField(upload_to='Artist_picture/', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Album(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(validators=[validate_year])
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='Album_cover_photo/', blank=True, null=True)
    
    def __str__(self):
        return f'{self.title} by {self.artist}'
    
