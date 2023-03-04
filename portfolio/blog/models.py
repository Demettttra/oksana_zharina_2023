from django.db import models

class category(models.Model):
    name=models.CharField(max_length=30)

class post(models.Model):
    title=models.CharField(max_length=30)
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    last_mod=models.DateTimeField(auto_now=True)
    categ=models.ManyToManyField('category', related_name='posts')

class comment(models.Model):
    author=models.CharField(max_length=50)
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey('post', on_delete=models.CASCADE)

