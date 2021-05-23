from rest_framework import serializers

from .models import Sale


class SaleSerializer(serializers.HyperlinkedModelSerializer):

    id = serializers.HyperlinkedIdentityField()
    created_at = serializers.TimeField()
    model_id = serializers.PrimaryKeyRelatedField()
    model_name = serializers.SlugRelatedField(read_only=True, slug_field="name")

    class Meta:
        model = Sale
        fields = "__all__"
        read_only_fields = ["id", "model_name"]
