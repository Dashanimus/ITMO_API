from api.httpbin_api import http_bin_api
from http import HTTPStatus


def test_time_out():
    res = http_bin_api.time_out(11)

    assert res.status_code == HTTPStatus.OK


def test_not_time():
    res = http_bin_api.time_out(2)

    assert not res[0]
