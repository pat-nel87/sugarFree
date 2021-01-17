from django.db import models
from django.contrib.auth.models import User

class Glucose(models.Model):
    reading = models.IntegerField()
    time = models.DateTimeField(auto_now_add=False)
    uploaded_by = models.ForeignKey(User,related_name="user_reading", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
