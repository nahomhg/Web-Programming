from django.db import models
from datetime import datetime

class Writer(models.Model):
    name = models.CharField(max_length=150)
    #articlesWritten = models.DecimalField(max_digits=10000, decimal_places=1)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200, null=True)
    body = models.TextField()
    datePosted = models.DateTimeField(default=datetime.today)
    writer = models.ForeignKey('Writer', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s " % (self.title, self.body)

# Create your models here.
