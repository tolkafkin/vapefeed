from django.http import Http404
from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from liquids.models import ManufacturerLiquid, Liquid
from liquids.serializers import ManufacturerLiquidSerializer, LiquidSerializer


@extend_schema(tags=['Изготовитель жидкости'])
class ManufacturerLiquidListCreateAPIView(GenericAPIView):
    queryset = ManufacturerLiquid.objects.all()
    serializer_class = ManufacturerLiquidSerializer

    @extend_schema(summary='Cписок')
    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @extend_schema(summary='Добавление')
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['Изготовитель жидкости'])
class ManufacturerLiquidAPIView(GenericAPIView):
    queryset = ManufacturerLiquid.objects.all()
    serializer_class = ManufacturerLiquidSerializer

    @extend_schema(summary='Получение')
    def get(self, request, pk):
        obj = self.get_queryset().get(pk=pk)
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    @extend_schema(summary='Редактирование')
    def put(self, request, pk):
        obj = self.get_queryset().get(pk=pk)
        serializer = self.get_serializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(summary='Удаление')
    def delete(self, request, pk):
        obj = self.get_queryset().get(pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@extend_schema(tags=['Жидкость'])
class LiquidListCreateAPIView(GenericAPIView):
    queryset = Liquid.objects.all()
    serializer_class = LiquidSerializer

    @extend_schema(summary='Список')
    def get(self, request):
        obj = self.get_queryset()
        serializer = self.get_serializer(obj, many=True)
        return Response(serializer.data)

    @extend_schema(summary='Добавление')
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['Жидкость'])
class LiquidAPIView(GenericAPIView):
    queryset = Liquid.objects.all()
    serializer_class = LiquidSerializer

    @extend_schema(summary='Получение')
    def get(self, request, pk):
        obj = self.get_queryset().get(pk=pk)
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    @extend_schema(summary='Редактирование')
    def put(self, request, pk):
        obj = self.get_queryset().get(pk=pk)
        serializer = self.get_serializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(summary='Частичное')
    def patch(self, request, pk):
        obj = self.get_queryset().get(pk=pk)
        serializer = self.get_serializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(summary='Удаление')
    def delete(self, request, pk):
        obj = self.get_queryset().get(pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
