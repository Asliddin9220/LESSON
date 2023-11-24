from datetime import timezone
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Publish'
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,choices=Status.choices,)

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
]
    default = Status.DRAFT

    def __str__(self) -> str:
        return self.title
class Media(models.Model):
    post =  models.ForeignKey(Post, on_delete=models.CASCADE)  
    image = models.ImageField(default= 'malibu.jpg')
 

 
     