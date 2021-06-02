from django.db import models


class Flashcard(models.Model):
    prompt = models.CharField(max_length=100, default=None)
    definition = models.CharField(max_length=400, default=None)
    collection = models.ForeignKey('card_collections.Collection', blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.prompt
