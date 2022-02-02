from turtle import up
from django.db.models.signals import post_save, post_delete

from .models import Molt, Spider


def updateCurrentMolt(sender, instance, **kwargs):
    molt = instance
    spider = molt.spider
    spider.current_molt = spider.molt_set.first().number
    spider.save()
    

post_save.connect(updateCurrentMolt, sender=Molt)
post_delete.connect(updateCurrentMolt, sender=Molt)