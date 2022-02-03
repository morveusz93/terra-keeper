from datetime import date
from django.db import models
from users.models import Profile
import uuid


class Spider(models.Model):
    SEX_CHOICES = (
        ('F', "Female"),
        ('M', "Male"),
        ('N', "Not sure")
    )
    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, null=True)
    genus = models.CharField(max_length=200)
    species = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    size = models.FloatField(blank=True, null=True)
    joined = models.DateField(default=date.today, blank=True)
    sex = models.CharField(max_length=1, blank=True,
                           null=True, choices=SEX_CHOICES, default="F")
    current_molt = models.IntegerField(null=True, blank=True)
    notes = models.TextField(max_length=2000, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return f"{self.name}, {self.genus[0].upper()}. {self.species.lower()}"
    

    @property
    def all_molts(self) -> list:
        "Returns the spider's molts."
        return [{'number': molt.number, 'date': molt.date, 'id': molt.id} for molt in self.molt_set.all()]
      
        

class Molt(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    spider = models.ForeignKey(Spider, on_delete=models.CASCADE, blank=True, null=True)
    date =  models.DateField(default=date.today, blank=True)
    number = models.IntegerField()

    def __str__(self):
        return f"{self.spider.name} - L{self.number}"

    class Meta:
        ordering = ['spider', '-number', '-date']
