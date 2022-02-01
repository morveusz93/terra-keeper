from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Spider
from .forms import SpiderForm, MoltForm


def spiders(request):
    spiders = Spider.objects.all()
    context = {'spiders': spiders}
    return render(request, 'spiders/index.html', context)


def details(request, id):
    spider = get_object_or_404(Spider, pk=id)
    try:
        new_molt_number = spider.current_molt + 1
    except TypeError:
        new_molt_number = 1
    form = MoltForm(initial={'number': new_molt_number})
    context = {'spider': spider, 'form': form}
    return render(request, 'spiders/details.html', context)


@login_required(login_url="login")
def createSpider(request):
    form = SpiderForm()
    if request.method == "POST":
        form = SpiderForm(request.POST)
        if form.is_valid():
            spider = form.save(commit=False)            
            spider.owner = request.user.profile
            spider.genus = spider.genus.capitalize()
            spider.species = spider.species.lower()
            spider.save()
        messages.success(request, "New spider successfully added! Good job!")
        return redirect('my-profile')

    context = {'form': form}
    return render(request, 'spiders/spider-form.html', context)


@login_required(login_url="login")
def updateSpider(request, id):
    spider = Spider.objects.get(id=id)
    form = SpiderForm(instance=spider)
    if request.method == "POST":
        form = SpiderForm(request.POST, instance=spider)
        if form.is_valid():
            messages.success(request, "Spider successfully updated ;)")
            form.save()
        return redirect('spider-details', id=id)

    context = {'form': form}
    return render(request, 'spiders/spider-form.html', context)


@login_required(login_url="login")
def deleteSpider(request, id):
    spider = Spider.objects.get(id=id)
    if request.method == "POST":
        spider.delete()
        messages.success(request, "Spider successfully deleted from your list.")
        return redirect('my-profile')
    context = {'obj': spider}
    return render(request, 'delete.html', context)


@login_required(login_url="login")
def molts(request, id):
    spider = Spider.objects.get(id=id)
    all_molts = spider.all_molts
    if request.method == 'POST':
        form = MoltForm(request.POST)
        if form.is_valid():
            new_molt = form.save(commit=False)
            new_molt.spider = spider
            new_molt.save()
            messages.success(request, "New molt added ;)")
        else:
            messages.error(request, "Error durning adding a molt, please try again.")
        
        return redirect('spider-details', id=id)

    context = {'all_molts': all_molts,'spider': spider}
    return render(request, 'spiders/spider-molts.html', context)