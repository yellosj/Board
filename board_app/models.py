from django.db import models

# Create your models here.

class Board(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=10, null=False)
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


