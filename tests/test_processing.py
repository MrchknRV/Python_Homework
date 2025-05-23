import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default(sample_state: list) -> None:
    assert filter_by_state(sample_state) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_canceled(sample_state: list) -> None:
    assert filter_by_state(sample_state, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_executed(sample_state: list) -> None:
    assert filter_by_state(sample_state, "EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_not_found(sample_state: list) -> None:
    assert filter_by_state(sample_state, "NOTFOUND") == []


def test_filter_by_state_empty() -> None:
    assert filter_by_state([]) == []


def test_filter_by_state_without_state(sample_state_without_state: list) -> None:
    assert filter_by_state(sample_state_without_state) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
    ]
    assert filter_by_state(sample_state_without_state, "CANCELED") == [
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
    ]


def test_sort_by_date_default(sample_date: list) -> None:
    assert sort_by_date(sample_date) == [
        {"id": 1, "state": "CANCELED", "date": "2025-03-26T17:37:18.419441"},
        {"id": 2, "state": "CANCELED", "date": "2020-10-14T03:14:25.412341"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 3, "state": "CANCELED", "date": "2019-02-26T15:17:33.568741"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_increasing(sample_date: list) -> None:
    assert sort_by_date(sample_date, False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 3, "state": "CANCELED", "date": "2019-02-26T15:17:33.568741"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "CANCELED", "date": "2020-10-14T03:14:25.412341"},
        {"id": 1, "state": "CANCELED", "date": "2025-03-26T17:37:18.419441"},
    ]


def test_sort_by_date_decreasing(sample_date: list) -> None:
    assert sort_by_date(sample_date, True) == [
        {"id": 1, "state": "CANCELED", "date": "2025-03-26T17:37:18.419441"},
        {"id": 2, "state": "CANCELED", "date": "2020-10-14T03:14:25.412341"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 3, "state": "CANCELED", "date": "2019-02-26T15:17:33.568741"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_empty() -> None:
    assert sort_by_date([], False) == []


def test_sort_by_date_missing_date(sample_date_missing_date: list) -> None:
    with pytest.raises(TypeError):
        sort_by_date(sample_date_missing_date)
