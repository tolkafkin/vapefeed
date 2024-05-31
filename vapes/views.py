from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from vapes.models import ManufacturerVape, Vape, VapeProfile
from vapes.serializers import ManufacturerVapeSerializer, VapeSerializer, VapeProfileSerializer


@extend_schema(request=ManufacturerVapeSerializer, tags=["Изготовитель вэйпа"])
class ManufacturerVapeListAPIView(APIView):
    @extend_schema(summary='Выдаёт список вендоров')
    def get(self, request):
        brands = ManufacturerVape.objects.all()
        serializer = ManufacturerVapeSerializer(brands, many=True)
        return Response(serializer.data)

    @extend_schema(summary='Создаёт новый вендер')
    def post(self, request):
        serializer = ManufacturerVapeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(request=ManufacturerVapeSerializer, tags=["Изготовитель вэйпа"])
class ManufacturerVapeDetailAPIView(APIView):
    @extend_schema(summary='Получение вендера')
    def get(self, request, pk):
        brand = ManufacturerVape.objects.get(pk=pk)
        serializer = ManufacturerVapeSerializer(brand)
        return Response(serializer.data)

    @extend_schema(summary='Редактирование вендора')
    def put(self, request, pk):
        brand = ManufacturerVape.objects.get(pk=pk)
        serializer = ManufacturerVapeSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(summary='Частичное редактирование вендора')
    def patch(self, request, pk):
        brand = ManufacturerVape.objects.get(pk=pk)
        serializer = ManufacturerVapeSerializer(brand, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(summary='Удаление вендора')
    def delete(self, request, pk):
        brand = ManufacturerVape.objects.get(pk=pk)
        brand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@extend_schema(request=VapeSerializer, tags=['Вэйп'])
class VapeListAPIView(APIView):
    @extend_schema(summary='Получение всех вэйпов')
    def get(self, request):
        devices = Vape.objects.all()
        serializer = VapeSerializer(devices, many=True)
        return Response(serializer.data)

    @extend_schema(summary='Создание вэйпа')
    def post(self, request):
        serializer = VapeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(request=VapeSerializer, tags=['Вэйп'])
class VapeDetailAPIView(APIView):
    @extend_schema(summary='Получение вэйпа')
    def get(self, request, pk):
        device = Vape.objects.get(pk=pk)
        serializer = VapeSerializer(device)
        return Response(serializer.data)

    @extend_schema(summary='Редактирование вэйпа')
    def put(self, request, pk):
        device = Vape.objects.get(pk=pk)
        serializer = VapeSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(summary='Частичное редактирование вэйпа')
    def patch(self, request, pk):
        device = Vape.objects.get(pk=pk)
        serializer = VapeSerializer(device, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(summary='Удаление вэйпа')
    def delete(self, request, pk):
        device = Vape.objects.get(pk=pk)
        device.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@extend_schema(request=VapeProfileSerializer, tags=['Вэйп-Профиль'])
class VapeProfileListAPIView(APIView):
    @extend_schema(summary='Получение списка вэйп-профилей')
    def get(self, request):
        vape_profiles = VapeProfile.objects.all()
        serializer = VapeProfileSerializer(vape_profiles, many=True)
        return Response(serializer.data)

    @extend_schema(summary='Создание вэйп-профиля')
    def post(self, request):
        serializer = VapeProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(request=VapeProfileSerializer, tags=['Вэйп-Профиль'])
class VapeProfileDetailAPIView(APIView):
    @extend_schema(summary='Получение вэйп-профиля')
    def get(self, request, pk):
        vape_profile = VapeProfile.objects.get(pk=pk)
        serializer = VapeProfileSerializer(vape_profile)
        return Response(serializer.data)

    @extend_schema(summary='Частичное редактирование вэйп-профиля')
    def patch(self, request, pk):
        vape_profile = VapeProfile.objects.get(pk=pk)
        serializer = VapeProfileSerializer(vape_profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(summary='Удаление вэйп-профиля')
    def delete(self, request, pk):
        vape_profile = VapeProfile.objects.get(pk=pk)
        vape_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
