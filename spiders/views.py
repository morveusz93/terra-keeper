from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView, RedirectView

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


class SpiderListView(ListView):
    model = Spider
    context_object_name = 'spider_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user.profile
        return context


    def get_queryset(self):
        return self.request.user.profile.spider_set.all()


class SpiderDetailView(DetailView):
    model = Spider
    context_object_name = 'spider'


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


class SpiderUpdateView(UpdateView):
    model = Spider
    form_class = SpiderForm

    def setup(self, request, *args, **kwargs):
        super(SpiderUpdateView, self).setup(request, *args, **kwargs)
        self.spider = Spider.objects.get(pk=kwargs['pk'])

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Spider successfully updated! Good job!")
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('spider-details', kwargs={'pk': self.spider.id})


class SpiderDeleteView(DeleteView):
    model = Spider
    template_name = 'delete.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('my-profile')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Molt successfully deleted.")
        return super().delete(request, *args, **kwargs)

# -----------------------------------MOLTS-----------------------------------

class MoltListView(ListView):
    model = Molt
    context_object_name = 'molt_list'

    def setup(self, request, *args, **kwargs):
        super(MoltListView, self).setup(request, *args, **kwargs)
        self.spider = Spider.objects.get(pk=kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['spider'] = self.spider
        return context

    def get_queryset(self):
        return self.spider.molt_set.all()


class MoltCreateView(CreateView):
    model = Molt
    form_class = MoltForm
    
    def setup(self, request, *args, **kwargs):
        super(MoltCreateView, self).setup(request, *args, **kwargs)
        self.spider = Spider.objects.get(pk=kwargs['pk'])
        self.new_molt_number = self.spider.get_next_molt_number()

    def get_success_url(self):
        return reverse_lazy('spider-details', kwargs={'pk': self.spider.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['spider'] = self.spider
        return context

    def get_initial(self):
        initial = super(MoltCreateView, self).get_initial()
        initial = initial.copy()
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
            messages.success(self.request, "New molt added ;)")
        else:
            messages.error(self.request, molt_validation_error)

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('spider-molts', kwargs={'pk': self.molt.spider.id})


class MoltDeleteView(DeleteView):
    model = Molt
    template_name = 'delete.html'
    context_object_name = 'obj'

    def setup(self, request, *args, **kwargs):
        super(MoltDeleteView, self).setup(request, *args, **kwargs)
        self.molt = Molt.objects.get(pk=kwargs['pk'])

    def get_success_url(self):
        return reverse_lazy('spider-molts', kwargs={'pk': self.molt.spider.id})

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Molt successfully deleted.")
        return super().delete(request, *args, **kwargs)