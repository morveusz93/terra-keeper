from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic import (DetailView, ListView, CreateView,
UpdateView, DeleteView, RedirectView, TemplateView)
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from spiders.custom_validators import molt_validator

from .models import Spider, Molt
from .forms import MoltForm, SpiderForm


class HomePageView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.pattern_name = "my-profile"
        else:
            self.pattern_name = "login"
        return super().get_redirect_url(*args, **kwargs)


@method_decorator(login_required, name='dispatch')
class SpiderListView(ListView):
    model = Spider
    context_object_name = 'spider_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user.profile
        return context

    def get_queryset(self):
        return self.request.user.profile.spider_set.all()


@method_decorator(login_required, name='dispatch')
class SpiderDetailView(DetailView):
    model = Spider
    context_object_name = 'spider'


@method_decorator(login_required, name='dispatch')
class SpiderCreateView(CreateView):
    model = Spider
    form_class = SpiderForm
    success_url = reverse_lazy('my-profile')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user.profile
        self.object.genus = self.object.genus.capitalize()
        self.object.species = self.object.species.lower()
        self.object.save()
        messages.success(self.request, "New spider successfully added! Good job!")
        return HttpResponseRedirect(self.get_success_url())


@method_decorator(login_required, name='dispatch')
class SpiderUpdateView(UpdateView):
    model = Spider
    form_class = SpiderForm

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.owner == self.request.user.profile:
            return super().get(request, *args, **kwargs)
        else:
            messages.error(self.request, "You can not edit that spider. It doesnt below to you!")
            return HttpResponseRedirect('/my-profile')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Spider successfully updated! Good job!")
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('spider-details', kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class SpiderDeleteView(DeleteView):
    model = Spider
    template_name = 'delete.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('my-profile')
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.owner == self.request.user.profile:
            return super().get(request, *args, **kwargs)
        else:
            messages.error(self.request, "You can not delete that spider. It doesnt below to you!")
            return HttpResponseRedirect('/my-profile')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Molt successfully deleted.")
        return super().delete(request, *args, **kwargs)

# -----------------------------------MOLTS-----------------------------------

@method_decorator(login_required, name='dispatch')
class MoltListView(ListView):
    model = Molt
    context_object_name = 'molt_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['spider'] = self.spider
        return context

    def get_queryset(self):
        self.spider = Spider.objects.get(pk=self.kwargs['pk'])
        return self.spider.molt_set.all()


@method_decorator(login_required, name='dispatch')
class MoltCreateView(CreateView):
    model = Molt
    form_class = MoltForm

    def get_success_url(self):
        return reverse('spider-details', kwargs={'pk': self.spider.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['spider'] = self.spider
        
        if self.spider.owner != self.request.user.profile:
            messages.error(self.request, "You can not add molt to that spider. It doesnt below to you!")
            return HttpResponseRedirect('/my-profile')

        return context

    def get_initial(self):
        initial = super(MoltCreateView, self).get_initial()
        initial = initial.copy()
        self.spider = Spider.objects.get(pk=self.kwargs['pk'])
        self.new_molt_number = self.spider.get_next_molt_number()
        initial['number'] = self.new_molt_number
        return initial

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.spider = self.spider
        molt_validation_error = molt_validator(self.object)
        if molt_validation_error is None:
            self.object.save()
            messages.success(self.request, "New molt added ;)")
        else:
            messages.error(self.request, molt_validation_error)

        return HttpResponseRedirect(self.get_success_url())


@method_decorator(login_required, name='dispatch')
class MoltUpdateView(UpdateView):
    model = Molt
    form_class = MoltForm

    def setup(self, request, *args, **kwargs):
        super(MoltUpdateView, self).setup(request, *args, **kwargs)
        self.molt = Molt.objects.get(pk=kwargs['pk'])
        self.update_molt_number = self.molt.number

    def form_valid(self, form):
        self.object = form.save(commit=False)
        molt_validation_error = molt_validator(self.object, update_molt=self.update_molt_number)
        if molt_validation_error is None:
            self.object.save()
            messages.success(self.request, "Molt updated! ;)")
        else:
            messages.error(self.request, molt_validation_error)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('spider-molts', kwargs={'pk': self.molt.spider.id})


@method_decorator(login_required, name='dispatch')
class MoltDeleteView(DeleteView):
    model = Molt
    template_name = 'delete.html'
    context_object_name = 'obj'

    def get_success_url(self):
        return reverse('spider-molts', kwargs={'pk': self.object.spider.id})

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Molt successfully deleted.")
        return super().delete(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class PhotoDeleteView(TemplateView):
    template_name = 'spiders/delete_photo.html'

    def setup(self, request, *args, **kwargs):
        super(PhotoDeleteView, self).setup(request, *args, **kwargs)
        self.spider = Spider.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['spider'] = self.spider
        return context

    def post(self, request, *args, **kwargs):
        self.spider.photo = None
        self.spider.save()
        return HttpResponseRedirect(reverse('spider-details', kwargs={'pk': self.spider.id}))