from datetime import date
from django.db import models
from users.models import Profile
import uuid
import os


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
    photo = models.ImageField(default='t-default.jpg')
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)


    __original_photo = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_photo = self.photo

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.photo != self.__original_photo:
            if self.__original_photo.name and self.__original_photo.name != 't-default.jpg':
                self.__original_photo.storage.delete(self.__original_photo.name)

        super().save(force_insert, force_update, *args, **kwargs)
        self.__original_photo = self.photo

    def __str__(self):
        return f"{self.name}, {self.genus[0].upper()}. {self.species.lower()}"
    
    @property
    def get_all_molts(self):
        "Returns the spider's molts."
        return [{'number': molt.number, 'date': molt.date, 'id': molt.id} for molt in self.molt_set.all()]

    @property
    def get_image(self):
        if not self.photo:
            return "/images/t-default.jpg"
        return self.photo.url

    def get_next_molt_number(self):
        try:
            new_molt_number = self.current_molt + 1
        except TypeError:
            new_molt_number = 1
        return new_molt_number

    def delete(self, using=None, keep_parents=False):
        if self.photo and self.photo.name != 't-default.jpg':
            self.photo.storage.delete(self.photo.name)
        super().delete()


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
