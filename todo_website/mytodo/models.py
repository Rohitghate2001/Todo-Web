from django.db import models
from datetime import datetime

# Create your models here.

class todo(models.Model):
    title=models.CharField( max_length=50)
    desc=models.TextField()
    completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(default=datetime.now())

    
