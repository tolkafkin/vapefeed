from django.urls import path

from liquids.views import LiquidListCreateAPIView, ManufacturerLiquidListCreateAPIView, ManufacturerLiquidAPIView, \
    LiquidAPIView

app_name = 'liquids'
urlpatterns = [
    path('', LiquidListCreateAPIView.as_view(), name='liquid-list'),
    path('<int:pk>/', LiquidAPIView.as_view(), name='liquid'),

    path('manufacturer/', ManufacturerLiquidListCreateAPIView.as_view(), name='manufacturer-list'),
    path('manufacturer/<int:pk>/', ManufacturerLiquidAPIView.as_view(), name='manufacturer'),
]