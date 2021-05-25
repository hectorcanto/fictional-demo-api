from datetime import datetime

from rest_framework.exceptions import ValidationError


def parse_since_until(request) -> (datetime, datetime):
    since = request.query_params.get("since")
    since = parse_interval(since, "since")

    until = request.query_params.get("until")
    until = parse_interval(until, "until")
    return since, until


def parse_interval(value: str, name: str):
    try:
        return str2month(value)
    except (ValueError, TypeError):
        raise ValidationError(f"{value} is not valid for '{name}' query parameter")


def str2month(value: str):
    if value is None:
        return value
    return datetime.strptime(value, "%Y/%m").date()
