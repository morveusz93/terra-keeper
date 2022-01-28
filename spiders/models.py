from django.db import models
import uuid


class Spider(models.Model):
    genus = models.CharField(max_length=200)
    species = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    molt = models.IntegerField(blank=True, null=True)
    size = models.FloatField(blank=True, null=True)
    added = models.DateField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f"{self.name}, {self.genus[0]}. {self.species} "
