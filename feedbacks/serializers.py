from rest_framework import serializers

from feedbacks.models import Feedback
from liquids.models import Liquid
from vapes.models import VapeProfile


class FeedbackSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    vape_profile = serializers.PrimaryKeyRelatedField(queryset=VapeProfile.objects.all())
    liquid = serializers.PrimaryKeyRelatedField(queryset=Liquid.objects.all())
    body = serializers.CharField()
    created = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Feedback.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.liquid = validated_data.get('liquid', instance.liquid)
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance
