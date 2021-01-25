from django.db import models
from django.contrib.auth.models import User

class Glucose(models.Model):
    reading = models.IntegerField()
    time = models.DateTimeField(auto_now_add=False)
    uploaded_by = models.ForeignKey(User,related_name="user_reading", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Insulin(models.Model):
    dose = models.IntegerField()
    time = models.DateTimeField(auto_now_add=False)
    uploaded_by = models.ForeignKey(User,related_name="user_dose", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Macro(models.Model):
    fat = models.IntegerField()
    carb = models.IntegerField()
    protein = models.IntegerField()
    time = models.DateTimeField(auto_now_add=False)
    calories = models.IntegerField(null=True, blank=True)
    uploaded_by = models.ForeignKey(User,related_name="user_macro", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)    
