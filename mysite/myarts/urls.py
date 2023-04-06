from django.urls import path 
from . import views 


app_name = 'myarts'
urlpatterns = [
    path('',  views.ArticleListView.as_view(), name = 'all'),
    path('create', views.ArticleCreateView.as_view(), name = 'article_create'),
    path('<int:pk>/update/', views.ArticleUpdateView.as_view(), name='article_update'),
    path('<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article_delete')
]