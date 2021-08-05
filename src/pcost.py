from pathlib import Path
from typing import Union
from .report import read_portfolio


def portfolio_cost(file_path: Union[str, Path]) -> float:
    """
    Calculates the cost of the portfolio by using the amount of shares
    and the corresponding price.

    :param file_path: Path to the portfolio file
    :return: The cost of the portfolio
    """
    portfolio = read_portfolio(file_path)
    return portfolio.total_cost
