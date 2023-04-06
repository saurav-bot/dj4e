from django.urls import path 
from django.views.generic import TemplateView
from . import views


app_name='crispy'
urlpatterns = [
    path('',TemplateView.as_view(template_name='crispy/main.html'), name='main'),
    path('boring', views.MyView.as_view(template_name='crispy/boring.html')),
    path('awesome', views.MyView.as_view(template_name='crispy/awesome.html'))
]