from django.urls import path

from vapes.views import ManufacturerVapeListAPIView, ManufacturerVapeDetailAPIView, VapeListAPIView, VapeDetailAPIView, \
    VapeProfileListAPIView, VapeProfileDetailAPIView

app_name = 'vapes'
urlpatterns = [
    path('', VapeListAPIView.as_view(), name='vape-list'),
    path('<int:pk>/', VapeDetailAPIView.as_view(), name='vape'),

    path('manufacturer/', ManufacturerVapeListAPIView.as_view(), name='manufacturer-list'),
    path('manufacturer/<int:pk>/', ManufacturerVapeDetailAPIView.as_view(), name='manufacturer'),

    path('profile/', VapeProfileListAPIView.as_view(), name='profile-list'),
    path('profile/<int:pk>/', VapeProfileDetailAPIView.as_view(), name='profile'),
]
