from django.shortcuts import render
from myarts.owner import OwnerCreateView, OwnerDeleteView, OwnerDetailView, OwnerListView, OwnerUpdateView
from .models import Article
from django.urls import reverse_lazy

# Create your views here.

class ArticleListView(OwnerListView):
    model = Article 

class ArticleCreateView(OwnerCreateView):
    model = Article
    fields = ['title', 'text']
    success_url = reverse_lazy('myarts:all')

class ArticleUpdateView(OwnerUpdateView):
    model = Article
    fields = ['title', 'text']
    success_url = reverse_lazy('myarts:all')

class ArticleDeleteView(OwnerDeleteView):
    model = Article
    fields = ['title', 'text']
    success_url = reverse_lazy('myarts:all')
