from rest_framework import serializers

from .models import Model


class PartSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField()
    name = serializers.CharField()

    class Meta:
        model = Model
        fields = ("id", "name")
        read_only_fields = ["id"]


class ModelSerializer(serializers.HyperlinkedModelSerializer):

    id = serializers.IntegerField()
    model_name = serializers.CharField()
    model_parts = PartSerializer(many=True)

    class Meta:
        model = Model
        fields = ("id", "model_name", "model_parts")
        read_only_fields = ["id", "model_parts"]
