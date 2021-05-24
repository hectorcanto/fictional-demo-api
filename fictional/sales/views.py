from rest_framework import renderers, mixins, viewsets

from .models import Sale
from .serializers import SaleSerializer


collection_conf = {"get": "list", "post": "create"}


class SalesViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    serializer_class = SaleSerializer
    renderer_classes = [renderers.JSONRenderer]
    queryset = Sale.objects.all()
