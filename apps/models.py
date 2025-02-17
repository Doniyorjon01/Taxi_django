from django.db import models

class Seat(models.Model):
    number = models.IntegerField(unique=True)
    is_taken = models.BooleanField(default=False)

