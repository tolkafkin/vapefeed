from django.urls import path, include
from rest_framework import routers

from .views import VapeViewSet, ManufacturerVapeViewSet, VapeProfileViewSet


router = routers.DefaultRouter()
router.register(r'vape', VapeViewSet, basename='vape')
router.register(r'manufacturer', ManufacturerVapeViewSet, basename='manufacturer')
router.register(r'profile-vape', VapeProfileViewSet, basename='profile_vape')


urlpatterns = [
    path('', include(router.urls)),
]
