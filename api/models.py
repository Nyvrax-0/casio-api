from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = (
        ('gshock', 'G-Shock'),
        ('edifice', 'Edifice'),
        ('vintage', 'Vintage'),
    )


    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name