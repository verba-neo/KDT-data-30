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
    # board/1/edit/
    path('<int:pk>/edit/', views.edit),
    # board/1/update/
    path('<int:pk>/update/', views.update),
    # board/1/delete/
    path('<int:pk>/delete/', views.delete),
]
