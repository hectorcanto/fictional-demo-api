from rest_framework import serializers

from .models import Model


class ModelSerializer(serializers.HyperlinkedModelSerializer):

    id = serializers.UUIDField()
    model_name = serializers.CharField()

    class Meta:
        model = Model
        fields = ("id", "model_name",)
        read_only_fields = ["id"]
