from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    TYPE_CHOICES = (
        ('text', 'Text'),
        ('audio', 'Audio'),
        ('video', 'Video'),
    )
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    note_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
