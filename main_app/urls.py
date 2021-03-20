from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
  path('', views.index, name="index"),
  path('about/', views.about, name="about"),
  path('contact/', views.contact, name='contact'),
  path('cats/', views.cats_index, name='cats')
]