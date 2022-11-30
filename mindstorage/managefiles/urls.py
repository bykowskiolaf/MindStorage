from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'managefiles'

urlpatterns = [
    path('', views.welcome_screen, name='welcome_screen'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('delete/<int:pk>/', views.file_delete, name='file_delete'),
    path('add_to_trash/<int:pk>/', views.add_to_trash, name='add_to_trash'),
    path('favourite/<int:pk>/', views.favourite, name='favourite'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)