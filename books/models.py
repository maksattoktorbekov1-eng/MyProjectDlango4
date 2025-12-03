from django.db import models

class WriterQuotes(models.Model):
    name = models.CharField(max_length=200)
    quote1 = models.TextField()
    quote2 = models.TextField()
    quote3 = models.TextField()
    quote4 = models.TextField()
    quote5 = models.TextField()

def __str__(self):
    return self.name
