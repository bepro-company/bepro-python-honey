from honey import dateutil
from datetime import datetime
import pytz


def test_to_iso_string_with_timezone():
    dt = dateutil.to_timezone(datetime(2021, 3, 4, 16, 11), "Asia/Seoul")

    assert dateutil.to_iso_string(dt) == "2021-03-04T07:11:00.000000Z"


def test_to_iso_string_without_timezone():
    dt = datetime(2021, 3, 4, 16, 25)

    assert dateutil.to_iso_string(dt) == "2021-03-04T16:25:00.000000Z"


def test_from_iso_string():
    dt = dateutil.from_iso_string("2021-03-04T16:26:00.000000Z")

    assert dt == datetime(2021, 3, 4, 16, 26, tzinfo=pytz.utc)


def test_to_timezone_with_timezone():
    tz = pytz.timezone("Asia/Seoul")
    dt = datetime(2021, 3, 4, 16, 32)
    dt = tz.localize(dt)

    assert dateutil.to_timezone(dt, "UTC") == datetime(2021, 3, 4, 7, 32, tzinfo=pytz.utc)


def test_to_timezone_without_timezone():
    dt = datetime(2021, 3, 4, 16, 36)

    assert dateutil.to_timezone(dt) == datetime(2021, 3, 4, 16, 36, tzinfo=pytz.utc)


def test_parse_datetime_without_timezone():
    assert dateutil.parse_datetime("2021-03-04T16:39") == datetime(2021, 3, 4, 16, 39, tzinfo=pytz.utc)
