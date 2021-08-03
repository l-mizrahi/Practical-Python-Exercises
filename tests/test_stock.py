from src.stock import Stock
import pytest


@pytest.fixture
def stock():
    return Stock("GOOG", 100, 490.10)


def test_stock_init(stock):
    assert stock.name == "GOOG"
    assert stock.shares == 100
    assert stock.price == 490.10


def test_stock_cost(stock):
    assert stock.cost() == 49010.0


def test_stock_sell(stock):
    stock.sell(25)
    assert stock.shares == 75
