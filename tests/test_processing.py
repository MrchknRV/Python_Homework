from src.processing import filter_by_state


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
