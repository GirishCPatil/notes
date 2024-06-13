from django.urls import path
from . import views

urlpatterns = [
  path('', views.get_datetime, name='current_datetime'),
]