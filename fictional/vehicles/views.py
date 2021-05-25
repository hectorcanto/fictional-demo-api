from datetime import datetime, date

from rest_framework import mixins, viewsets, renderers
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from fictional.sales.models import Sale
from .models import Model
from .parsers import parse_since_until
from .serializers import ModelSerializer

RANGE_TYPES = ["day", "week", "month", "year"]


class ModelsViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """A CRUD view set without a Edition capabilities"""

    serializer_class = ModelSerializer
    renderer_classes = [renderers.JSONRenderer]
    queryset = Model.objects.all()


class ModelSalesView(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """A List endpoint for Sales of a model"""

    since = None
    until = None

    def get_queryset(self):
        queryset = Sale.objects.all()
        self.since, self.until = parse_since_until(self.request)
        # TODO filter by model pk
        interval = {}
        if self.since:
            interval["created_at__gte"] = self.since
        if self.until:
            interval["created_at__lte"] = self.until
        if interval:
            return queryset.filter(**interval)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        count = queryset.count()

        avg_range = request.query_params.get("average", "month")
        average = period = None

        if avg_range not in RANGE_TYPES:
            raise ValidationError(f"{avg_range} is not a valid 'average' value")
        if count:
            first_occurrence = queryset.first().created_at.date()
            average, period = compute_average(
                count, first_occurrence, self.since, self.until, avg_range
            )

        skip = True if request.query_params.get("skip") in ["1", "true", "t"] else False
        if skip:
            return Response({"count": count, "average": average, "period": period})

        return Response(
            {
                "data": queryset,  # TODO serialize all
                "count": count,
                "average": average,
                "period": period,
            }
        )  # TODO JSONAPI style serializer


def compute_average(count: int, first: datetime, since: date, until: date, range_type: str):
    old = since if since else first
    new = until if until else date.today()
    interval = (new - old).days

    divider = 30
    if range_type == "year":
        divider = 365
    elif range_type == "day":
        divider = 1
    elif range_type == "week":
        divider = 7

    interval = interval / divider
    return round(count / interval, 2), f"{round(interval,2)} {range_type}"


collection_conf = {"get": "list", "post": "creates"}

detail_conf = {"get": "retrieve", "delete": "destroy"}

sales_conf = {"get": "list"}
