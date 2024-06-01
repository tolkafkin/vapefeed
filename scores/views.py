from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.response import Response

from scores.models import Score, UserFeedbackScore, LiquidFeedbackScore
from scores.serializers import ScoreSerializer, UserFeedbackScoreSerializer, LiquidFeedbackScoreSerializer


@extend_schema(tags=['Рейтинг'])
class ScoreListAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

    @extend_schema(summary='Список')
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(summary='Добавление')
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


@extend_schema(tags=['Рейтинг'])
class ScoreDetailAPIView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

    @extend_schema(summary='Получение')
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(summary='Частичное редактирование')
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(summary='Удаление')
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


@extend_schema(tags=['Рейтинг отзыва'])
class UserFeedbackScoreListAPIView(ListModelMixin,
                               CreateModelMixin,
                               GenericAPIView):
    queryset = UserFeedbackScore.objects.all()
    serializer_class = UserFeedbackScoreSerializer

    @extend_schema(summary='Список')
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @extend_schema(summary='Добавление')
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


@extend_schema(tags=['Рейтинг отзыва'])
class UserFeedbackScoreDetailAPIView(RetrieveModelMixin,
                                     UpdateModelMixin,
                                     DestroyModelMixin,
                                     GenericAPIView):
    queryset = UserFeedbackScore.objects.all()
    serializer_class = UserFeedbackScoreSerializer

    @extend_schema(summary='Получение')
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @extend_schema(summary='Редактирование')
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(summary='Частичное')
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(summary='Удаление')
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


@extend_schema(tags=['Рейтинг жидкости'])
class LiquidFeedbackScoreListAPIView(ListModelMixin,
                                     CreateModelMixin,
                                     GenericAPIView):
    queryset = LiquidFeedbackScore.objects.all()
    serializer_class = LiquidFeedbackScoreSerializer

    @extend_schema(summary='Список')
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(summary='Добавление')
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


@extend_schema(tags=['Рейтинг жидкости'])
class LiquidFeedbackScoreDetailAPIView(RetrieveModelMixin,
                                       UpdateModelMixin,
                                       DestroyModelMixin,
                                       GenericAPIView):
    queryset = LiquidFeedbackScore.objects.all()
    serializer_class = LiquidFeedbackScoreSerializer

    @extend_schema(summary='Получение')
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(summary='Редактирование')
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(summary='Частичное')
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(summary='Удаление')
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
