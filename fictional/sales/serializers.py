from rest_framework import serializers

from fictional.vehicles.models import Model, Vehicle
from .models import Sale, Office
from fictional.vehicles.serializers import BasicModelSerializer


class OfficeSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField()
    address = serializers.CharField()
    phone = serializers.CharField()
    region = serializers.CharField()  # TODO add django-country or simillar for it

    class Meta:
        model = Sale
        fields = ["id", "address", "region", "phone"]
        read_only_fields = ["id",]


class SaleSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)  # TODO serialize to Timestamp
    model_id = serializers.PrimaryKeyRelatedField(read_only=True, source="model")
    vehicle_id = serializers.PrimaryKeyRelatedField(read_only=True, source="vehicle")
    office_id = serializers.PrimaryKeyRelatedField(read_only=True, source="office")
    model = BasicModelSerializer(read_only=True)
    office = OfficeSerializer(read_only=True)
    # TODO office can be taken from user requesting

    class Meta:
        model = Sale
        fields = ["id", "model", "office", "id", "vehicle_id", "created_at", "office_id", "model_id"]
        read_only_fields = ["id", "model", "office"]

    def create(self, validated_data):

        model_id = self.initial_data["model_id"]
        vehicle_id = self.initial_data.get("vehicle_id")
        office_id = self.initial_data["office_id"]

        extra = dict(model=Model.objects.get(pk=model_id), office=Office.objects.get(pk=office_id))
        if vehicle_id:
            extra["vehicle"] = Vehicle.objects.get(pk=vehicle_id)
        return Sale.objects.create(**validated_data, **extra)
