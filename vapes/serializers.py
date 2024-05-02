from rest_framework.serializers import ModelSerializer

from .models import Vape, ManufacturerVape, VapeProfile


class VapeSerializer(ModelSerializer):
    class Meta:
        model = Vape
        fields = '__all__'


class ManufactureVapeSerializer(ModelSerializer):
    class Meta:
        model = ManufacturerVape
        fields = '__all__'


class VapeProfileSerializer(ModelSerializer):
    class Meta:
        model = VapeProfile
        fields = '__all__'
