from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images', validators=[FileExtensionValidator(['png'])])
    
    def __str__(self):
        return self.name