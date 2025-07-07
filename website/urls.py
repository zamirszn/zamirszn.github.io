
from django import views
from django.urls import path

from website import views


urlpatterns = [
    path('', views.portfolio, name='portfolio'),
]