from django.db.models.signals import post_save, post_delete
from .models import Molt, Spider

def updateCurrentMolt(sender, instance, **kwargs):
    molt = instance
    try:
        spider = molt.spider
        if len(spider.molt_set.all()) > 0:
            spider.current_molt = spider.molt_set.first().number
        else:
            spider.current_molt = None
        spider.save()
    except Spider.DoesNotExist:
        pass

post_save.connect(updateCurrentMolt, sender=Molt)
post_delete.connect(updateCurrentMolt, sender=Molt)