import pytest
from src.report import (
    get_report,
    read_portfolio,
    read_prices,
    calc_gain_loss,
    make_report,
    portfolio_report,
)
from src import DATA_DIRECTORY


def test_read_portfolio():
    """
    Tests if read_portfolio constructs each entry in the list correctly.
    """
    portfolio = read_portfolio(DATA_DIRECTORY / "portfolio.csv")
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


def test_read_portfolio_missing_values():
    """
    Tests if read_portfolio raises a ValueError if there is a blank line in the file.
    """
    with pytest.raises(ValueError):
        read_portfolio(DATA_DIRECTORY / "missing.csv")


def test_read_prices():
    """
    Tests if read_prices constructs the dictionary of prices correctly.
    """
    prices = read_prices(DATA_DIRECTORY / "prices.csv")
    prices = dict(list(prices.items())[:5])
    expected = {"AA": 9.22, "AXP": 24.85, "BA": 44.85, "BAC": 11.27, "C": 3.72}

    assert prices == expected


def test_calc_gain_loss():
    """
    Tests if calc_gain_loss calculates the change in price correctly
    and inserts it into the new dictionary.
    """
    prices = read_prices(DATA_DIRECTORY / "prices.csv")
    portfolio = read_portfolio(DATA_DIRECTORY / "portfolio.csv")

    expected = [-22.98, 15.18, -47.98, -30.34, -26.89, -44.21, 35.84]

    gain_loss = calc_gain_loss(portfolio, prices)

    assert all([round(gl["change"], 2) == e for gl, e in zip(gain_loss, expected)])


def test_make_report():
    """
    Tests if make_report formats the portfolio correctly.
    """
    prices = read_prices(DATA_DIRECTORY / "prices.csv")
    portfolio = read_portfolio(DATA_DIRECTORY / "portfolio.csv")
    report = make_report(portfolio, prices)

    expected = [
        ("AA", 100, 9.22, -22.98),
        ("IBM", 50, 106.28, 15.18),
        ("CAT", 150, 35.46, -47.98),
        ("MSFT", 200, 20.89, -30.34),
        ("GE", 95, 13.48, -26.89),
        ("MSFT", 50, 20.89, -44.21),
        ("IBM", 100, 106.28, 35.84),
    ]

    assert report == expected


def test_get_report():
    """
    Tests if get_report generates the correct looking table.
    """
    prices = read_prices(DATA_DIRECTORY / "prices.csv")
    portfolio = read_portfolio(DATA_DIRECTORY / "portfolio.csv")
    report = make_report(portfolio, prices)
    printed_report = get_report(report)

    expected = [
        "      Name     Shares      Price     Change",
        "---------- ---------- ---------- ----------",
        "        AA        100       9.22     -22.98",
        "       IBM         50     106.28      15.18",
        "       CAT        150      35.46     -47.98",
        "      MSFT        200      20.89     -30.34",
        "        GE         95      13.48     -26.89",
        "      MSFT         50      20.89     -44.21",
        "       IBM        100     106.28      35.84",
    ]

    assert printed_report == expected


def test_portfolio_report():
    report = portfolio_report(
        DATA_DIRECTORY / "portfolio.csv", DATA_DIRECTORY / "prices.csv"
    )
    expected = [
        "      Name     Shares      Price     Change",
        "---------- ---------- ---------- ----------",
        "        AA        100       9.22     -22.98",
        "       IBM         50     106.28      15.18",
        "       CAT        150      35.46     -47.98",
        "      MSFT        200      20.89     -30.34",
        "        GE         95      13.48     -26.89",
        "      MSFT         50      20.89     -44.21",
        "       IBM        100     106.28      35.84",
    ]

    assert report == expected
