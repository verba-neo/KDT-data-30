from django.urls import path
from . import views

# URL을 변수로 사용하기 => app_name:name 
app_name = 'crud'

urlpatterns = [
    # /univ/new/
    path('new/', views.new, name='new'),  # crud:new
    # /univ/create/
    path('create/', views.create, name='create'),  # crud:create
    # /univ/
    path('', views.index, name='index'),  # crud:index
    # /univ/1/
    path('<int:pk>/', views.detail, name='detail'),  # crud:detail
    # /univ/1/edit/
    path('<int:pk>/edit/', views.edit, name='edit'),  # crud:edit
    # /univ/1/update/
    path('<int:pk>/update/', views.update, name='update'),  # crud:update
    # /univ/1/delete/
    path('<int:pk>/delete/', views.delete, name='delete'),  # crud:delete
]
    
