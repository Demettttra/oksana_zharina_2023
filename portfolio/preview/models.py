from django.db import models

class project(models.Model):
    title=models.CharField(max_length=30)
    description=models.CharField(max_length=30)
    tags=models.CharField(max_length=25)
    image=models.FileField(upload_to='img/')
