from django.db import models


# Create your models here.
class Flashcard(models.Model):
    prompt = models.CharField(max_length=100, default=None)
    definition = models.CharField(max_length=400, default=None)
    collection = models.ForeignKey('Collection', blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.prompt


class Collection(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name
