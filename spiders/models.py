from django.db import models


class Spider(models.Model):
    genus = models.CharField(max_length=200)
    species = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    molt = models.IntegerField(blank=True, null=True)
    size = models.FloatField(blank=True, null=True)
    added = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name}, {self.genus[0]}. {self.species} "
