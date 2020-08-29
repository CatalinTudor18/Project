from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Enjoy/', views.Enjoy, name='Enjoy'),
    path('Home/', views.Home, name='Home'),
    path('Upcoming_year/', views.Upcoming_year, name='Upcoming_year'),
    path('How/', views.How, name='How'),
    path('About/', views.About, name='About'),
    path('CV/',views.CV, name='CV'),
    path('sent/',views.CV, name='sent'),

    re_path(r'^(?P<year>[0-9]{4})/(?P<month>0?[1-9]|1[0-2])/', views.index, name='index'),
]
