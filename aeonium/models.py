from django.db import models
from mdeditor.fields import MDTextField

class Blog(models.Model):
    title = models.CharField(max_length=50)
    text = MDTextField()
    date = models.DateField(auto_now_add=True)


