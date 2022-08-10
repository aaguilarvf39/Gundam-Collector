from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('gundams/', views.gundams_index, name='index'),
  path('gundams/<int:gundam_id>/', views.gundams_detail, name='detail'),
  path('gundams/create/', views.GundamCreate.as_view(), name='gundams_create'),
  path('gundams/<int:pk>/update/', views.GundamUpdate.as_view(), name='gundams_update'),
  path('gundams/<int:pk>/delete/', views.GundamDelete.as_view(), name='gundams_delete'),
  path('gundams/<int:gundam_id>/add_repair/', views.add_repair, name='add_repair'),
]