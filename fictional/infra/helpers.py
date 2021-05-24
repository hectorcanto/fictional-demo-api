from datetime import datetime, timezone


def dt_now():
    return datetime.now(tz=timezone.utc)
