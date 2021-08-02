from src import DATA_DIRECTORY
from src.fileparse import parse_csv


def test_parse_csv():
    portfolio = parse_csv(DATA_DIRECTORY / "portfolio.csv")
    expected = [
        {"name": "AA", "shares": "100", "price": "32.20"},
        {"name": "IBM", "shares": "50", "price": "91.10"},
        {"name": "CAT", "shares": "150", "price": "83.44"},
        {"name": "MSFT", "shares": "200", "price": "51.23"},
        {"name": "GE", "shares": "95", "price": "40.37"},
        {"name": "MSFT", "shares": "50", "price": "65.10"},
        {"name": "IBM", "shares": "100", "price": "70.44"},
    ]

    assert portfolio == expected


def test_parse_csv_select():
    portfolio = parse_csv(DATA_DIRECTORY / "portfolio.csv", select=["name", "shares"])
    expected = [
        {"name": "AA", "shares": "100"},
        {"name": "IBM", "shares": "50"},
        {"name": "CAT", "shares": "150"},
        {"name": "MSFT", "shares": "200"},
        {"name": "GE", "shares": "95"},
        {"name": "MSFT", "shares": "50"},
        {"name": "IBM", "shares": "100"},
    ]

    assert portfolio == expected


def test_parse_csv_types():
    portfolio = parse_csv(DATA_DIRECTORY / "portfolio.csv", types=[str, int, float])
    expected = [
        {"name": "AA", "shares": 100, "price": 32.2},
        {"name": "IBM", "shares": 50, "price": 91.1},
        {"name": "CAT", "shares": 150, "price": 83.44},
        {"name": "MSFT", "shares": 200, "price": 51.23},
        {"name": "GE", "shares": 95, "price": 40.37},
        {"name": "MSFT", "shares": 50, "price": 65.1},
        {"name": "IBM", "shares": 100, "price": 70.44},
    ]

    assert portfolio == expected


def test_parse_csv_select_types():
    portfolio = parse_csv(
        DATA_DIRECTORY / "portfolio.csv", select=["name", "shares"], types=[str, int]
    )
    expected = [
        {"name": "AA", "shares": 100},
        {"name": "IBM", "shares": 50},
        {"name": "CAT", "shares": 150},
        {"name": "MSFT", "shares": 200},
        {"name": "GE", "shares": 95},
        {"name": "MSFT", "shares": 50},
        {"name": "IBM", "shares": 100},
    ]

    assert portfolio == expected
