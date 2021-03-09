from datetime import datetime

import dateutil.parser
import pytz


def to_iso_string(input_datetime):
    utc_datetime = to_utc(input_datetime)
    return datetime.strftime(utc_datetime, "%Y-%m-%dT%H:%M:%S.{:06d}Z").format(utc_datetime.microsecond)


def from_iso_string(iso_string):
    return dateutil.parser.parse(iso_string)


def to_timezone(input_datetime, timezone="UTC"):
    tz = pytz.timezone(timezone)

    if input_datetime.tzinfo:
        return input_datetime.astimezone(tz)

    return tz.localize(input_datetime)


def to_utc(input_datetime):
    return to_timezone(input_datetime, "UTC")


def to_cet(input_datetime):
    return to_timezone(input_datetime, "CET")


def parse_datetime(dt, timezone="UTC"):
    dt = from_iso_string(dt)

    if dt and not dt.tzinfo:
        dt = to_timezone(dt, timezone)

    return dt


def now(timezone="UTC"):
    return to_timezone(datetime.utcnow(), timezone)
