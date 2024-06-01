from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, \
    DestroyAPIView
from rest_framework.views import APIView

from feedbacks.models import Feedback
from feedbacks.serializers import FeedbackSerializer


class FeedbackBase(GenericAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


@extend_schema(tags=['Отзыв'])
class FeedbackListCreateAPIView(ListAPIView, CreateAPIView, FeedbackBase):

    @extend_schema(summary='Добавление')
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    @extend_schema(summary='Список')
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


@extend_schema(tags=['Отзыв'])
class FeedbackDetailAPIView(RetrieveAPIView, UpdateAPIView, DestroyAPIView, FeedbackBase):

    @extend_schema(summary='Получение')
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(exclude=True)
    def put(self, request, *args, **kwargs):
        pass

    @extend_schema(summary='Частичное')
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(summary='Удаление')
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
