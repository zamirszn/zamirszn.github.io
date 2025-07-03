
from django import views
from django.urls import path

from website import views


urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
]