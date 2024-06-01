from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers

from feedbacks.models import Feedback
from liquids.models import Liquid
from scores.models import Score, UserFeedbackScore, LiquidFeedbackScore


@extend_schema_serializer()
class ScoreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
    created = serializers.DateTimeField(read_only=True)
    value = serializers.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    def create(self, validated_data):
        return Score.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.value = validated_data.get('value', instance.value)
        instance.save()
        return instance


@extend_schema_serializer()
class BaseScoreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    score = serializers.PrimaryKeyRelatedField(queryset=Score.objects.all())

    def update(self, instance, validated_data):
        instance.score = validated_data.get('score', instance.score)
        instance.save()
        return instance

    class Meta:
        abstract = True


@extend_schema_serializer()
class UserFeedbackScoreSerializer(BaseScoreSerializer):
    feedback = serializers.PrimaryKeyRelatedField(queryset=Feedback.objects.all())

    def create(self, validated_data):
        return UserFeedbackScore.objects.create(**validated_data)


@extend_schema_serializer()
class LiquidFeedbackScoreSerializer(BaseScoreSerializer):
    liquid = serializers.PrimaryKeyRelatedField(queryset=Liquid.objects.all())

    def create(self, validated_data):
        return LiquidFeedbackScore.objects.create(**validated_data)
