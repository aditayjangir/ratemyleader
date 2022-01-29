from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class PoliticianDetail(models.Model):
    first_name=models.CharField(max_length=255) 
    last_name =models.CharField(max_length=255)
    likes = models.JSONField(User, default=None, blank=True)
    photo=models.ImageField(upload_to='media/Polititcian_images/')


    def total_likes(self):
        return self.likes.count()
    def __str__(self):
        return self.first_name
