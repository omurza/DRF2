from django.shortcuts import render
from rest_framework.generics import (ListAPIView, CreateAPIView, 
                                     UpdateAPIView, DestroyAPIView, RetrieveAPIView,
                                     ListCreateAPIView, RetrieveUpdateDestroyAPIView)

from .models import NewsKg
from .serializers import SettingsNewsKg
# Create your views here.
class SettingsCreateApi(CreateAPIView):
    queryset=NewsKg.objects.all()
    serializer_class=SettingsNewsKg
class SettingsUpdateApi(UpdateAPIView):
    queryset=NewsKg.objects.all()
    serializer_class=SettingsNewsKg
class SettingsRetieveApi(RetrieveAPIView):
    queryset=NewsKg.objects.all()
    serializer_class=SettingsNewsKg
class SettingsDestroyApi(DestroyAPIView):
    queryset=NewsKg.objects.all()
    serializer_class=SettingsNewsKg
class SettingslistApi(ListAPIView):
    queryset=NewsKg.objects.all()
    serializer_class=SettingsNewsKg