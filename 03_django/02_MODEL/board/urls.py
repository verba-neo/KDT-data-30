# board/urls.py

from django.urls import path
from . import views


urlpatterns = [
    # board/new/
    path('new/', views.new),
    # board/create/
    path('create/', views.create),
    # board/
    path('', views.index),
    # board/1/
    path('<int:pk>/', views.detail),
    # board/edit/
    path('edit/', views.edit),
    # board/update/
    path('update/', views.update),
    # board/delete/
    path('delete/', views.delete),
]
