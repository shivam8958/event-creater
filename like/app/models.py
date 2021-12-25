from django.db import models

# Create your models here.
class event(models.Model):
    e_name=models.CharField(max_length=150)
    dat=models.DateTimeField()
    location=models.CharField(max_length=150)
    des=models.CharField(max_length=200)
    image=models.ImageField(upload_to='album')
    def __str__(self):
        return self.e_name


