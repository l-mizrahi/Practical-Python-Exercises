from pathlib import Path
from typing import Any, Dict, Union, cast, List
from .fileparse import parse_csv
from .stock import Stock


def portfolio_cost(file_path: Union[str, Path]) -> float:
    """
    Calculates the cost of the portfolio by using the amount of shares
    and the corresponding price.

    :param file_path: Path to the portfolio file
    :return: The cost of the portfolio
    """
    portfolio = parse_csv(
        file_path,
        select=["shares", "price"],
        convert_fn={"shares": int, "price": float},
    )
    portfolio = cast(List[Dict[str, Any]], portfolio)
    total_cost = sum([p["shares"] * p["price"] for p in portfolio])

    return total_cost
