from django.shortcuts import get_object_or_404, redirect, render
from .models import Spider
from .forms import SpiderForm
from django.contrib.auth.decorators import login_required


def spiders(request):
    spiders = Spider.objects.all()
    context = {'spiders': spiders}
    return render(request, 'spiders/index.html', context)


def details(request, id):
    spider = get_object_or_404(Spider, pk=id)
    print(spider)
    context = {'spider': spider}
    return render(request, 'spiders/details.html', context)


@login_required(login_url="login")
def createSpider(request):
    form = SpiderForm()
    if request.method == "POST":
        form = SpiderForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('spiders')

    context = {'form': form}
    return render(request, 'spiders/spider-form.html', context)


@login_required(login_url="login")
def updateSpider(request, id):
    spider = Spider.objects.get(id=id)
    form = SpiderForm(instance=spider)
    if request.method == "POST":
        form = SpiderForm(request.POST, instance=spider)
        if form.is_valid():
            form.save()
        return redirect('spider-details', id=id)

    context = {'form': form}
    return render(request, 'spiders/spider-form.html', context)


@login_required(login_url="login")
def deleteSpider(request, id):
    spider = Spider.objects.get(id=id)
    if request.method == "POST":
        spider.delete()
        return redirect("spiders")
    context = {'obj': spider}
    return render(request, 'delete.html', context)
