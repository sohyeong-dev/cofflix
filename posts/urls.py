from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.main, name='main'),
    path('host/', views.host, name='host'),
    path('lists/', views.lists, name='lists'),
]
