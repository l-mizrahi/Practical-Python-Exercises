import csv
from pathlib import Path
from typing import Union
import logging


def portfolio_cost(file_path: Union[str, Path]) -> float:
    """
    Calculates the cost of the portfolio by using the amount of shares
    and the corresponding price.

    :param file_path: Path to the portfolio file
    :return: The cost of the portfolio
    """
    total_cost = 0.0
    with open(file_path) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, 1):
            if not row:
                continue
            rowdict = dict(zip(headers, row))
            try:
                shares = int(rowdict["shares"])
                price = float(rowdict["price"])
                total_cost += shares * price

            # Exercise asks to catch the error like this
            except ValueError:
                logging.exception(f"Could not process row number {rowno}: {rowdict}")

    return total_cost
