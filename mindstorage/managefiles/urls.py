from django.urls import path

from . import views

app_name = 'managefiles'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('delete/<int:pk>/', views.file_delete, name='file_delete'),
    path('add_to_trash/<int:pk>/', views.add_to_trash, name='add_to_trash'),
    path('favourite/<int:pk>/', views.favourite, name='favourite'),

]
