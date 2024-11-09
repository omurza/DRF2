from django.urls import path
from .views import *

urlpatterns = [
    # CRUD
    path('', SettingslistApi.as_view(), name="settings list api"),
    path('create/', SettingsCreateApi.as_view(), name="settings create api"),
    path('<int:pk>/', SettingsRetieveApi.as_view(), name="settings retrieve api"),
    path('update/<int:pk>/', SettingsUpdateApi.as_view(), name="settings update api"),
    path('delete/<int:pk>/', SettingsDestroyApi.as_view(), name="settings delete api"),
]