from src.stock import Stock
import pytest


@pytest.fixture
def stock():
    return Stock("GOOG", 100, 490.10)


def test_stock_init(stock):
<<<<<<< HEAD
    """
    Tests if Stock initializes attributes correctly.
    """
=======
>>>>>>> 8ecf7aa (tests(ex4.2): add tests for Stock class)
    assert stock.name == "GOOG"
    assert stock.shares == 100
    assert stock.price == 490.10


def test_stock_cost(stock):
<<<<<<< HEAD
    """
    Tests if Stock calculates cost correctly.
    """
    assert stock.cost == 49010.0


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
    assert repr(stock) == "Stock(name='GOOG', shares=100, price=490.1)"


def test_stock_shares_setter(stock):
    """
    Test if TypeError raised if shares is assigned to non-integer.
    """
    with pytest.raises(TypeError):
        stock.shares = 100.2
=======
    assert stock.cost() == 49010.0


def test_stock_sell(stock):
    stock.sell(25)
    assert stock.shares == 75
>>>>>>> 8ecf7aa (tests(ex4.2): add tests for Stock class)
