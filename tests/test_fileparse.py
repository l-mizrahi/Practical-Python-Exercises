from src import DATA_DIRECTORY
import pytest
from src.fileparse import parse_csv


def test_parse_csv():
    """
    Tests if parse_csv reads a file correctly.
    """
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
    """
    Tests if parse_csv selects the correct columns.
    """
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
    """
    Tests if parse_csv converts columns to the correct types.
    """
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
    """
    Tests if parse_csv selects the correct columns and converts them correctly.
    """
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


def test_parse_csv_noheaders():
    """
    Tests if parse_csv reads a file correctly with no headers.
    """
    records = parse_csv(DATA_DIRECTORY / "prices.csv", has_headers=False)
    expected = [
        ("AA", "9.22"),
        ("AXP", "24.85"),
        ("BA", "44.85"),
        ("BAC", "11.27"),
        ("C", "3.72"),
        ("CAT", "35.46"),
        ("CVX", "66.67"),
        ("DD", "28.47"),
        ("DIS", "24.22"),
        ("GE", "13.48"),
        ("GM", "0.75"),
        ("HD", "23.16"),
        ("HPQ", "34.35"),
        ("IBM", "106.28"),
        ("INTC", "15.72"),
        ("JNJ", "55.16"),
        ("JPM", "36.90"),
        ("KFT", "26.11"),
        ("KO", "49.16"),
        ("MCD", "58.99"),
        ("MMM", "57.10"),
        ("MRK", "27.58"),
        ("MSFT", "20.89"),
        ("PFE", "15.19"),
        ("PG", "51.94"),
        ("T", "24.79"),
        ("UTX", "52.61"),
        ("VZ", "29.26"),
        ("WMT", "49.74"),
        ("XOM", "69.35"),
    ]

    assert records == expected


def test_parse_csv_types_noheaders():
    """
    Tests if parse_csv reads a file correctly with no headers and converts the columns correctly.
    """
    records = parse_csv(
        DATA_DIRECTORY / "prices.csv", types=[str, float], has_headers=False
    )
    expected = [
        ("AA", 9.22),
        ("AXP", 24.85),
        ("BA", 44.85),
        ("BAC", 11.27),
        ("C", 3.72),
        ("CAT", 35.46),
        ("CVX", 66.67),
        ("DD", 28.47),
        ("DIS", 24.22),
        ("GE", 13.48),
        ("GM", 0.75),
        ("HD", 23.16),
        ("HPQ", 34.35),
        ("IBM", 106.28),
        ("INTC", 15.72),
        ("JNJ", 55.16),
        ("JPM", 36.90),
        ("KFT", 26.11),
        ("KO", 49.16),
        ("MCD", 58.99),
        ("MMM", 57.10),
        ("MRK", 27.58),
        ("MSFT", 20.89),
        ("PFE", 15.19),
        ("PG", 51.94),
        ("T", 24.79),
        ("UTX", 52.61),
        ("VZ", 29.26),
        ("WMT", 49.74),
        ("XOM", 69.35),
    ]

    assert records == expected


def test_parse_csv_hasheaders():
    """
    Tests if parse_csv reads a file correctly with headers.
    """
    records = parse_csv(DATA_DIRECTORY / "portfolio.csv", has_headers=True)
    expected = [
        {"name": "AA", "shares": "100", "price": "32.20"},
        {"name": "IBM", "shares": "50", "price": "91.10"},
        {"name": "CAT", "shares": "150", "price": "83.44"},
        {"name": "MSFT", "shares": "200", "price": "51.23"},
        {"name": "GE", "shares": "95", "price": "40.37"},
        {"name": "MSFT", "shares": "50", "price": "65.10"},
        {"name": "IBM", "shares": "100", "price": "70.44"},
    ]

    assert records == expected


def test_parse_csv_space_delimiter():
    """
    Tests if parse_csv reads a file correctly with different delimiters.
    """
    expected = [
        {"name": "AA", "shares": "100", "price": "32.20"},
        {"name": "IBM", "shares": "50", "price": "91.10"},
        {"name": "CAT", "shares": "150", "price": "83.44"},
        {"name": "MSFT", "shares": "200", "price": "51.23"},
        {"name": "GE", "shares": "95", "price": "40.37"},
        {"name": "MSFT", "shares": "50", "price": "65.10"},
        {"name": "IBM", "shares": "100", "price": "70.44"},
    ]

    records = parse_csv(DATA_DIRECTORY / "portfolio.dat", delimiter=" ")
    assert records == expected

    records = parse_csv(DATA_DIRECTORY / "portfolio.csv", delimiter=",")
    assert records == expected


def test_parse_csv_select_noheaders():
    """
    Tests if parse_csv raises a RuntimeError if both select and has no headers.
    """
    with pytest.raises(ValueError):
        parse_csv(
            DATA_DIRECTORY / "portfolio.csv",
            select=["name", "price"],
            has_headers=False,
        )
