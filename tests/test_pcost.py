from src.pcost import portfolio_cost
from src import DATA_DIRECTORY


def test_portfolio_cost():
    """
    Tests if portfolio_cost calculates the cost of a portfolio correctly.
    """
    assert portfolio_cost(DATA_DIRECTORY / "portfolio.csv") == 44671.15


def test_portfolio_cost_missing_values(caplog):
    """
    Tests if portfolio_cost raises a ValueError if there are blank lines in the file.
    """
    cost = portfolio_cost(DATA_DIRECTORY / "missing.csv")
    assert cost == 27381.15


def test_portfolio_cost_different_headers():
    """
    Tests if portfolio_cost calculates the correct cost given a different file format.
    """
    assert portfolio_cost(DATA_DIRECTORY / "portfoliodate.csv") == 44671.15


def test_portfolio_cost_incorrect_format(caplog):
    """
    Tests if portfolio_cost logs rows that cannot be converted.
    """
    cost = portfolio_cost(DATA_DIRECTORY / "portfolio3.csv")
    assert cost == 9121.25
