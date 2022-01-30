import uuid
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=500)

    def __str__(self):
        return str(self.username)
