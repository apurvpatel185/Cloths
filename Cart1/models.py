from django.db import models

# Create your models here.
class Rentdays(models.Model):
    days = models.DecimalField(decimal_places=2,max_digits=20,max_length=20)

    def __str__(self):
        return self.days
