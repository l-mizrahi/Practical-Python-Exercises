from typing import Counter
from src.stock import Stock
from src.portfolio import Portfolio
import pytest


@pytest.fixture
def stock_data():
    stock_data = [
        Stock(name="AA", shares=100, price=32.2),
        Stock(name="IBM", shares=50, price=91.1),
        Stock(name="CAT", shares=150, price=83.44),
        Stock(name="MSFT", shares=200, price=51.23),
        Stock(name="GE", shares=95, price=40.37),
        Stock(name="MSFT", shares=50, price=65.1),
        Stock(name="IBM", shares=100, price=70.44),
    ]

    return stock_data


def test_portfolio_init(stock_data):
    """
    Tests if Portfolio initializes correctly.
    """
    portfolio = Portfolio(stock_data)
    assert portfolio._holdings == stock_data


def test_portfolio_total_cost(stock_data):
    """
    Tests if Portfolio calculates total cost of holdings correctly.
    """
    portfolio = Portfolio(stock_data)
    assert portfolio.total_cost == 44671.15


def test_portfolio_tabulate_shares(stock_data):
    """
    Tests if Portfolio returns the correct count of shares.
    """
    portfolio = Portfolio(stock_data)
    counts = {
        "AA": 100,
        "IBM": 150,
        "CAT": 150,
        "MSFT": 250,
        "GE": 95,
    }
    expected_counter = Counter(counts)
    assert expected_counter == portfolio.tabulate_shares()
