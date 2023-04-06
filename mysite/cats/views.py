from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cat, Breed
from django.urls import reverse_lazy
# Create your views here.

class CatView(LoginRequiredMixin, ListView):
    model = Cat 
    success_url=reverse_lazy('cats:all')

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['breed_count'] = Breed.objects.all().count()
        return context
    

class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat 
    fields='__all__'
    success_url=reverse_lazy('cats:all')

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat 
    fields='__all__'
    success_url=reverse_lazy('cats:all')


class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    success_url=reverse_lazy('cats:all')
    fields='__all__'



class BreedView(LoginRequiredMixin, ListView):
    model = Breed 

class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed 
    fields='__all__'
    success_url=reverse_lazy('cats:all')


class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed 
    fields='__all__'
    success_url=reverse_lazy('cats:all')


class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    success_url=reverse_lazy('cats:all')
    fields='__all__'
