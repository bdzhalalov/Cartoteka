from django.db import models


class Card(models.Model):
    series = models.PositiveIntegerField()
    number = models.PositiveBigIntegerField()
    release_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField()
    last_usage = models.DateTimeField(auto_now=True)
    amount = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=32, default='not activated')

    def __str__(self):
        return f'{self.number}'
