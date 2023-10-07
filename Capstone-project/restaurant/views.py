from django.shortcuts import render
from.serializers import BookingSerializer, MenuSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking, Menu
from rest_framework import generics, viewsets, permissions


# Create your views here.

def index (request):
    return render(request, 'index.html', {})
        
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]