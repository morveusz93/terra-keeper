from django.shortcuts import get_object_or_404, render
from .models import Spider


def home(request):
    spiders = Spider.objects.all()
    context = {'spiders': spiders}
    return render(request, 'spiders/index.html', context)

def details(request, id):
    spider = get_object_or_404(Spider, pk=id)
    print(spider)
    context = {'spider': spider}
    return render(request, 'spiders/details.html', context)

def new(request):
    return render(request, 'spider-form.html')