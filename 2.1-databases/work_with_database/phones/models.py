from django.db import models


class Phone(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=70)
    price = models.PositiveIntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=70)
