from django.shortcuts import render
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.viewsets import ModelViewSet

from .models import Vape, ManufacturerVape, VapeProfile
from .serializers import VapeSerializer, ManufactureVapeSerializer, VapeProfileSerializer


@extend_schema_view(
    list=extend_schema(
        summary="Получение списка вэйпов",
        description="""
        Этот эндпоинт необходим для получения списка всех вэйп девайсов находящихся в базе данных.
        """,
        tags=['Вэйп'],
    ),
    create=extend_schema(
        summary='Добавление одного вэйпа',
        description="""
        Этот эндпоинт необходим для добавления одного вэйп девайса в базу данных.
        """,
        tags=['Вэйп'],
    ),
    retrieve=extend_schema(
        summary='Получение одного вэйпа',
        description="""
        Этот эндпоинт необходим для просмотра и получения одного вэйп девайса.
        """,
        tags=['Вэйп'],
    ),
    update=extend_schema(
        summary="Редактирование одного вэйпа",
        description="""
        Этот эндпоинт необходим для полного изменения информации (редактирования) одного вэйп девайса.
        """,
        tags=['Вэйп'],
    ),
    partial_update=extend_schema(
        summary='Частичное редактирование одного вэйпа',
        description="""
        Этот эндпоинт необходим для частичного редактирования или некоторых пунктов информации у одного вэйп девайса.
        """,
        tags=['Вэйп'],
    ),
    destroy=extend_schema(
        summary='Удаление одного вэйпа',
        description="""
        Этот эндпоинт необходим для полного удаления одного вэйп девайса.
        """,
        tags=['Вэйп'],
    ),
)
class VapeViewSet(ModelViewSet):
    serializer_class = VapeSerializer
    queryset = Vape.objects.all()


@extend_schema_view(
    list=extend_schema(
        summary="Получение списка изготовителей вэйп девайсов",
        description="""
        Этот эндпоинт необходим для получения списка изготовителей вэйп девайсов.
        """,
        tags=['Изготовитель вэйпа'],
    ),
    create=extend_schema(
        summary='Добавление изготовителя вэйп девайсов',
        description="""
        Этот эндпоинт необходим для добавления одного изготовителя вэйп девайсов.
        """,
        tags=['Изготовитель вэйпа'],
    ),
    retrieve=extend_schema(
        summary='Получение одного изготовителя вэйп девайса',
        description="""
        Этот эндпоинт необходим для просмотра и получения одного изготовителя вэйп девайсов из базы данных.
        """,
        tags=['Изготовитель вэйпа'],
    ),
    update=extend_schema(
        summary="Редактирование одного изготовителя вэйп девайса",
        description="""
        Этот эндпоинт необходим для редактирования изготовителя вэйп девайса.
        """,
        tags=['Изготовитель вэйпа'],
    ),
    partial_update=extend_schema(
        summary='Частичное редактирование изготовителя вэйп девайса',
        description="""
        Этот эндпоинт необходим для частичного редактирования или некоторых пунктов информации у одного изготовителя 
        вэйп девайса.
        """,
        tags=['Изготовитель вэйпа'],
    ),
    destroy=extend_schema(
        summary='Удаление одного изготовителя вэйп девайса',
        description="""
        Этот эндпоинт необходим для полного удаления одного изготовителя вэйп девайса из базы данных.
        """,
        tags=['Изготовитель вэйпа'],
    ),
)
class ManufacturerVapeViewSet(ModelViewSet):
    serializer_class = ManufactureVapeSerializer
    queryset = ManufacturerVape.objects.all()


@extend_schema_view(
    list=extend_schema(
        summary="Получение списка вэйп-профилей",
        description="""
        Этот эндпоинт необходим для получения списка всех вэйп-профилей, где содержится информация об пользователе и 
        девайсе, которым он пользуется.
        """,
        tags=['Вэйп-профайл'],
    ),
    create=extend_schema(
        summary='Добавление одного вэйп-профайла',
        description="""
        Этот эндпоинт необходим для добавления одного вэйп-профайла, связывает профиль пользователя с девайсом.
        Связывает профиль пользователя с имеющимися в базе данных вэйп девайсов, без дубилкатов.
        Например:
            1 профиль - 1 девайс под номер 103,
            Нельзя связать этот же профиль с этим же девайсов под номером 103.
        """,
        tags=['Вэйп-профайл'],
    ),
    retrieve=extend_schema(
        summary='Получение одного вэйп-профайла',
        description="""
        Этот эндпоинт необходим для просмотра вэйп-профайла и содержащейся в нём информации.
        """,
        tags=['Вэйп-профайл'],
    ),
    update=extend_schema(
        summary="Редактирование одного вэйп-профайла",
        description="""
        Этот эндпоинт необходим для редактирования одного вэйп-профайла и содержащейся в нём информации.
        """,
        tags=['Вэйп-профайл'],
    ),
    partial_update=extend_schema(
        summary='Частичное редактирование одного вэйп-профайла',
        description="""
        Этот эндпоинт необходим для частичного редактирования или некоторых пунктов информации у одного вэйп-профайла.
        """,
        tags=['Вэйп-профайл'],
    ),
    destroy=extend_schema(
        summary='Удаление одного вэйп-профайла',
        description="""
        Этот эндпоинт необходим для полного удаления одного вэйп-профайла.
        """,
        tags=['Вэйп-профайл'],
    ),
)
class VapeProfileViewSet(ModelViewSet):
    serializer_class = VapeProfileSerializer
    queryset = VapeProfile.objects.all()
