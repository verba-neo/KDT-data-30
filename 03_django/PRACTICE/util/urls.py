from django.urls import path
from . import views

urlpatterns = [
    # util/
    path('', views.index),
    # util/time/
    path('time/', views.time),
]
