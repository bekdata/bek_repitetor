from django.db import models

# Create your models here.
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField()
    about = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name