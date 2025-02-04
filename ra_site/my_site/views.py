from rest_framework import generics
from django.shortcuts import render
from my_site.serializers import AcidSerializer, RecksonSerializer, MainSerializer

from my_site.models import AcidInfo, RecksonInfo, Gameprogress, MainInfo

# Create your views here.

class MainAPIView(generics.ListAPIView):
    queryset = MainInfo.objects.all()
    serializer_class = MainSerializer


class AcidAPIView(generics.ListAPIView):
    queryset = AcidInfo.objects.all()
    serializer_class = AcidSerializer


class RecksonAPIView(generics.ListAPIView):
    queryset = RecksonInfo.objects.all()
    serializer_class = RecksonSerializer
