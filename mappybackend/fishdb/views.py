from django.shortcuts import render
from rest_framework import generics
from .models import Fish, FishPosition
from .serializer import FishSerializer, FishPositionSerializer

# Create your views here.
class FishListCreateAPIView(generics.ListCreateAPIView):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer

class FishDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer
    lookup_field = 'PIT_code'

class FishPositionbyATCodeAPI(generics.ListAPIView):
    serializer_class = FishPositionSerializer

    def get_queryset(self):
        AT_code = self.kwargs['AT_code']
        return FishPosition.objects.filter(fish__AT_code=AT_code).order_by('timestamp')