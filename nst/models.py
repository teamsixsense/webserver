from django.db import models


# Create your models here.
class Picmodel(models.Model):
    class Meta:
        db_table = "pictures"

    image = models.ImageField()
    name = models.CharField(max_length=256)
    artist = models.CharField(max_length=256, null=True)
    desc = models.TextField(null=True)
    nation = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.name
