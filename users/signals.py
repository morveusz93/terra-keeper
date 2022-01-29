from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import Profile
from spiders.models import AnimalsList


def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            name=user.username,
            email=user.email,
        )
        print("profile created")

def createAnimalsList(sender, instance, created, **kwargs):
    if created:
        profile = instance
        animalsList = AnimalsList.objects.create(
            owner = profile
        )
        print("list created")

def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()
    print('deleted user')


post_save.connect(createProfile, sender=User)
post_save.connect(createAnimalsList, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)
