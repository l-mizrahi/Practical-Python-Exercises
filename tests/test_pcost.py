from src.pcost import portfolio_cost
from src import DATA_DIRECTORY
import logging


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
    expected_error = [
        (
            "root",
            logging.ERROR,
            "Could not process row number 4: {'name': 'MSFT', 'shares': '', 'price': '51.23'}",
        ),
        (
            "root",
            logging.ERROR,
            "Could not process row number 7: {'name': 'IBM', 'shares': '', 'price': '70.44'}",
        ),
    ]

    assert caplog.record_tuples == expected_error
    assert cost == 27381.15


def test_portfolio_cost_different_headers():
    """
    Tests if portfolio_cost calculates the correct cost given a different file format.
    """
    assert portfolio_cost(DATA_DIRECTORY / "portfoliodate.csv") == 44671.15


def test_portfolio_cost_incorrect_format(caplog):
    """
    Tests if portfolio_cost raises a ValueError if type conversion cannot be done.
    """
    cost = portfolio_cost(DATA_DIRECTORY / "portfolio3.csv")
    expected_error = [
        (
            "root",
            logging.ERROR,
            "Could not process row number 2: {'name': 'HPQ', 'shares': '250', 'price': 'forty'}",
        )
    ]

    assert caplog.record_tuples == expected_error
    assert cost == 9121.25
