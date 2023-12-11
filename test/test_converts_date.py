from src.converts_date import converts_date


def test_converts_date():
    assert converts_date("2019-08-26T10:50:58.294041") == "26.08.2019"
