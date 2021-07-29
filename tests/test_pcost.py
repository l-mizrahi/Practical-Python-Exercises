import pytest
from src.pcost import portfolio_cost


def test_portfolio_cost():
    """
    Tests if portfolio_cost calculates the cost of a portfolio correctly.
    """
    assert portfolio_cost("data/portfolio.csv") == 44671.15


def test_portfolio_cost_missing_values():
    """
    Tests if portfolio_cost raises a ValueError if there are blank lines in the file.
    """
    with pytest.raises(ValueError):
        portfolio_cost("data/missing.csv")


def test_portfolio_cost_different_headers():
    """
    Tests if portfolio_cost calculates the correct cost given a different file format.
    """
    assert portfolio_cost("data/portfoliodate.csv") == 44671.15


def test_portfolio_cost_incorrect_format():
    """
    Tests if portfolio_cost raises a ValueError if type conversion cannot be done.
    """
    with pytest.raises(ValueError):
        portfolio_cost("data/portfolio3.csv")
