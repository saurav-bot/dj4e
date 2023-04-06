from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class OwnerListView(LoginRequiredMixin, ListView):
    """ list views"""


class OwnerDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        query =  super().get_queryset()
        return query.filter(owner=self.request.user)
class OwnerCreateView(LoginRequiredMixin, CreateView):
    def form_valid(self, form):
        object = form.save(commit=False)
        object.owner = self.request.user
        return super().form_valid(form)

class OwnerUpdateView(LoginRequiredMixin, UpdateView):
    def get_queryset(self):
        query =  super().get_queryset()
        return query.filter(owner=self.request.user)
    
class OwnerDeleteView(LoginRequiredMixin, DeleteView):
    def get_queryset(self):
        query = super().get_queryset()
        return query.filter(owner=self.request.user)