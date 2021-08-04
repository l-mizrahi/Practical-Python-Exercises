from pathlib import Path
from typing import Union
from .fileparse import parse_csv
from .stock import Stock


def portfolio_cost(file_path: Union[str, Path]) -> float:
    """
    Calculates the cost of the portfolio by using the amount of shares
    and the corresponding price.

    :param file_path: Path to the portfolio file
    :return: The cost of the portfolio
    """
    portdict = parse_csv(
        file_path,
        select=["shares", "price"],
        convert_fn={"shares": int, "price": float},
    )
    portfolio = [
        Stock(name="", shares=pd["shares"], price=pd["price"])
        for pd in portdict
        if isinstance(pd, dict)
    ]
    total_cost = sum([p.shares * p.price for p in portfolio])

    return total_cost
