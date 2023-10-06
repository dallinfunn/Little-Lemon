from django.urls import path
from . import views
from rest_framework import routers

urlpatterns = [
   path('', views.index, name='index'),
   path('menu/', views.MenuView.as_view()),
   path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]