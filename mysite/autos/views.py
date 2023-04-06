from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import MakeForm
from django.urls import reverse_lazy
from .models import Make, Auto

# Create your views here.

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        mk = Make.objects.all().count()
        al = Auto.objects.all()
        ctx = {
            'make_count':mk,
            'auto_list': al
        }
        return render(request, 'autos/auto_list.html', ctx)
    
class MakeView(LoginRequiredMixin, View):
    def get(self, request):
        mk = Make.objects.all()
        ctx = {
            'make_list':mk
        }

        return render(request, 'autos/make_list.html', ctx)
    
class MakeCreate(LoginRequiredMixin, View):
    template_name = 'autos/make_form.html'
    success_url = reverse_lazy('autos:all')

    def get(self, request):
        form = MakeForm()
        ctx = {
            'form': form
        }
        return render(request, self.template_name, ctx)
    

    def post(self, request):
        form = MakeForm(request.POST)
        if not form.is_valid():
            ctx = {
                'form': form 
            }
            return render(request, self.template_name, ctx)

        make = form.save()
        return redirect(self.success_url)
    
class MakeUpdate(LoginRequiredMixin, View):
    template_name = 'autos/make_form.html'
    success_url = reverse_lazy('autos:all')
    model = Make 

    def get(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(instance = make)

        ctx = {
            'form': form 
        }

        return render(request, self.template_name, ctx)

    def post(self, request, pk):
        make = get_object_or_404(Make, pk=pk)
        form = MakeForm(request.POST, instance=make)
        if not form.is_valid():
            ctx = {
                'form':form
            }
            return render(request, self.template_name, ctx)

        make = form.save()

        return redirect(self.success_url)
    

class MakeDelete(LoginRequiredMixin, View):
    template_name = 'autos/make_confirm_delete.html'
    success_url = reverse_lazy('autos:all')

    def get(self, request, pk):
        make = get_object_or_404(Make, pk=pk)
        form = MakeForm(make)
        ctx = {'form':form}

        return render(request, self.template_name, ctx)

    def post(self, request, pk):
        make = get_object_or_404(Make, pk=pk)
        make.delete()

        return redirect(self.success_url)


class AutoCreate(LoginRequiredMixin, CreateView):
    model=Auto
    fields='__all__'
    success_url=reverse_lazy('autos:all')

class AutoUpdate(LoginRequiredMixin, UpdateView):
    model=Auto
    fields='__all__'
    success_url=reverse_lazy('autos:all')

class AutoDelete(LoginRequiredMixin, DeleteView):
    model=Auto
    fields='__all__'
    success_url=reverse_lazy('autos:all')
    
