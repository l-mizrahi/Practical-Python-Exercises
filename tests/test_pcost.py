from src.pcost import portfolio_cost
from src import DATA_DIRECTORY


def test_portfolio_cost():
    """
    Tests if portfolio_cost calculates the cost of a portfolio correctly.
    """
    assert portfolio_cost(DATA_DIRECTORY / "portfolio.csv") == 44671.15


def test_portfolio_cost_missing_values(capfd):
    """
    Tests if portfolio_cost raises a ValueError if there are blank lines in the file.
    """
    cost = portfolio_cost(DATA_DIRECTORY / "missing.csv")
    out, err = capfd.readouterr()

    assert cost == 27381.15
    assert (
        out.strip("\n")
        == "Row 4: Bad row {'name': 'MSFT', 'shares': '', 'price': '51.23'}\n\
Row 7: Bad row {'name': 'IBM', 'shares': '', 'price': '70.44'}"
    )


def test_portfolio_cost_different_headers():
    """
    Tests if portfolio_cost calculates the correct cost given a different file format.
    """
    assert portfolio_cost(DATA_DIRECTORY / "portfoliodate.csv") == 44671.15


def test_portfolio_cost_incorrect_format(capfd):
    """
    Tests if portfolio_cost raises a ValueError if type conversion cannot be done.
    """
    cost = portfolio_cost(DATA_DIRECTORY / "portfolio3.csv")
    out, err = capfd.readouterr()

    assert cost == 9121.25
    assert (
        out.strip("\n")
        == "Row 2: Bad row {'name': 'HPQ', 'shares': '250', 'price': 'forty'}"
    )
