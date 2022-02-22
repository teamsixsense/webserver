from django.db import models


# Create your models here.
class Picmodel(models.Model):
    class Meta:
        db_table = "pictures"

    image = models.ImageField()
    name = models.CharField(null=True)
    artist = models.CharField(null=True)
    desc = models.TextField(null=True)
    nation = models.CharField()
