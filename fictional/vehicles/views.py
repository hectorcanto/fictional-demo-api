from rest_framework import mixins, viewsets, renderers

from fictional.sales.models import Sale
from .models import Model
from .serializers import ModelSerializer

from datetime import datetime, date
from rest_framework.exceptions import ValidationError

collection_conf = {
    "get": "list",
    "post": "creates"
}

detail_conf = {
    "get": "retrieve",
    "delete": "destroy"
}


class ModelViewset(
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


RANGE_TYPES = ["day", "week", "month", "year"]


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
        breakpoint()
        # TODO filter by model pk
        interval = {}
        if self.since:
            interval["created_at__gte"] = self.since
        if self.until:
            interval["created_at__lte"] = self.until
        if interval:
            return queryset.filter(**interval)
        return queryset

    def list(self,  request, *args, **kwargs):
        breakpoint()
        queryset = self.get_queryset()
        count = queryset.count()
        average = None
        if count:
            first_occurrence = queryset.first().created_at
            avg_range = request.query_params.get("average", "month")
            if avg_range not in RANGE_TYPES:
                raise ValidationError(f"{avg_range} is not a valid 'average' value")
            average = compute_average(count, first_occurrence, self.since, self.until, avg_range)

        skip = True
        if skip:
            return {
                "count": count,
                "average": average,
            }

        return {
            "data": queryset,  # TODO serialize all
            "count": count,
            "average": average,
        }  # TODO JSONAPI style serializer


def compute_average(count: int, first: datetime, since: date, until: date, range_type: str):

    today = datetime.now()
    a = since if since else first
    b = until if until else today
    interval = (b - a).days()

    divider = 30
    if range_type == "year":
        divider = 365
    elif range_type == "day":
        divider = 1
    elif range_type == "week":
        divider = 7

    return count * divider / interval


def parse_since_until(request) -> (datetime, datetime):
    since = request.query_params.get("since")
    since = parse_interval(since, "since")

    until = request.query_params.get("until")
    until = parse_interval(until, "until")
    return since, until


def parse_interval(value, name):
    try:
        return str2month(value)
    except:
        raise ValidationError(f"{value} is not valid for '{name}' query parameter")


def str2month(value):
    return datetime.strptime(value, '%Y/%m/01').date()