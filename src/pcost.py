from pathlib import Path
from typing import Union
from .fileparse import parse_csv


def portfolio_cost(file_path: Union[str, Path]) -> float:
    """
    Calculates the cost of the portfolio by using the amount of shares
    and the corresponding price.

    :param file_path: Path to the portfolio file
    :return: The cost of the portfolio
    """
    portfolio = parse_csv(file_path, select=["shares", "price"], types=[int, float])
    total_cost = sum([p["shares"] * p["price"] for p in portfolio])

    return total_cost
