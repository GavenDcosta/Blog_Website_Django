from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=200, default='annonymous')
    title = models.CharField(max_length = 300)
    body = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self) -> str:
        return self.title
