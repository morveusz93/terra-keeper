from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Spider, Molt
from .forms import SpiderForm, MoltForm
from .custom_validators import molt_validator


# ----------------------------SPIDERS----------------------------

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

# ----------------------------MOLTS----------------------------

@login_required(login_url="login")
def molts(request, id):
    spider = Spider.objects.get(id=id)
    all_molts = spider.all_molts        
    context = {'all_molts': all_molts, 'spider': spider}
    return render(request, 'spiders/spider-molts.html', context)


@login_required(login_url="login")
def createMolt(request, id):
    spider = Spider.objects.get(id=id)
    try:
        new_molt_number = spider.current_molt + 1
    except TypeError:
        new_molt_number = 1
    form = MoltForm(initial={'number': new_molt_number })
    if request.method == 'POST':
        form = MoltForm(request.POST)
        if form.is_valid():
            new_molt = form.save(commit=False)
            new_molt.spider = spider
            molt_validation_error = molt_validator(new_molt)
            if molt_validation_error is None:
                new_molt.save()
                messages.success(request, "New molt added ;)")
            else:
                messages.error(request, molt_validation_error)
                return redirect('molts', id=id)
        else:
            messages.error(request, "Error durning adding a molt, please try again.")
        
        return redirect('molts', id=id)

    context = {'spider': spider, 'form': form}
    return render(request, 'spiders/molt-form.html', context)


@login_required(login_url="login")
def updateMolt(request, molt_id):
    molt = Molt.objects.get(id=molt_id)
    spider = molt.spider
    form = MoltForm(instance=molt)
    if request.method == "POST":
        form = MoltForm(request.POST, instance=molt)
        if form.is_valid():
            updated_molt = form.save(commit=False)
            molt_validation_error = molt_validator(updated_molt, update=True)
            if molt_validation_error is None:
                updated_molt.save()
                messages.success(request, "Molt updated!")
            else:
                messages.error(request, molt_validation_error)
                return redirect('molts', id=spider.id)

        return redirect('molts', id=spider.id)

    context = {'form': form, 'spider': spider}
    return render(request, 'spiders/molt-form.html', context)


@login_required(login_url="login")
def deleteMolt(request, molt_id):
    molt = Molt.objects.get(id=molt_id)
    spider = molt.spider
    if request.method == "POST":
        molt.delete()
        messages.success(request, "Molt successfully deleted.")
        return redirect('molts', spider.id)
    context = {'obj': molt}
    return render(request, 'delete.html', context)

