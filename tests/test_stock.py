from src.stock import Stock
import pytest


@pytest.fixture
def stock():
    return Stock("GOOG", 100, 490.10)


def test_stock_init(stock):
    """
    Tests if Stock initializes attributes correctly.
    """
    assert stock.name == "GOOG"
    assert stock.shares == 100
    assert stock.price == 490.10


def test_stock_cost(stock):
    """
    Tests if Stock calculates cost correctly.
    """
    assert stock.cost() == 49010.0


def test_stock_sell(stock):
    """
    Tests if Stock sells the correct amount of shares.
    """
    stock.sell(25)
    assert stock.shares == 75


def test_stock_repr(stock):
    """
    Test if __repr__ method returns correct string.
    """
    assert repr(stock) == "Stock('GOOG', 100, 490.1)"
