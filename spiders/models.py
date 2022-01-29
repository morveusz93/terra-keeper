from datetime import date
from django.db import models
from users.models import Profile
import uuid


class AnimalsList(models.Model):
    owner = models.OneToOneField(Profile, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return f"{self.owner}'s list"


class Spider(models.Model):
    list = models.ForeignKey(
        AnimalsList, on_delete=models.CASCADE, blank=True, null=True)
    genus = models.CharField(max_length=200)
    species = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    molt = models.IntegerField(blank=True, null=True)
    size = models.FloatField(blank=True, null=True)
    joined = models.DateField(default=date.today, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return f"{self.name}, {self.genus[0]}. {self.species} "
