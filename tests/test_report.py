from src.pcost import portfolio_cost
import pytest
from src.report import read_portfolio, read_prices


def test_read_portfolio():
    portfolio = read_portfolio("data/portfolio.csv")
    expected = [
        {"name": "AA", "shares": 100, "price": 32.2},
        {"name": "IBM", "shares": 50, "price": 91.1},
        {"name": "CAT", "shares": 150, "price": 83.44},
        {"name": "MSFT", "shares": 200, "price": 51.23},
        {"name": "GE", "shares": 95, "price": 40.37},
        {"name": "MSFT", "shares": 50, "price": 65.1},
        {"name": "IBM", "shares": 100, "price": 70.44},
    ]

    assert len(portfolio) == len(expected)
    assert all([p == e for p, e in zip(portfolio, expected)])


def test_read_portfolio_missing_values():
    with pytest.raises(ValueError):
        portfolio_cost("data/missing.csv")


def test_read_prices():
    prices = read_prices("data/prices.csv")
    prices = dict(list(prices.items())[:5])
    expected = {"AA": 9.22, "AXP": 24.85, "BA": 44.85, "BAC": 11.27, "C": 3.72}

    assert prices == expected


def test_read_prices_missing_values():
    with pytest.raises(ValueError):
        read_prices("data/prices.csv")
