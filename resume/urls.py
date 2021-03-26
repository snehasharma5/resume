from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('msg/', views.message_from_viewer, name='msg'),
]
