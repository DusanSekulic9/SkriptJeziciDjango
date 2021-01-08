from django.urls import path
from . import views

app_name = 'baza_telefoni'
urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.articles, name='articles'),
    path('articles/<int:id>/', views.article, name='article'),
    path('article/edit/<int:id>/', views.edit, name='edit'),
    path('article/new/', views.new, name='new'),
    path('article/delete/<int:id>/', views.delete, name='delete'),
    path('signup/', views.signup, name='signup')
]