from django.shortcuts import render
from rest_framework import generics
from .models import Fish
from .serializer import FishSerializer

# Create your views here.
class FishListCreateAPIView(generics.ListCreateAPIView):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer

class FishDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer
    lookup_field = 'PIT_code'
