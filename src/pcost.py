import csv


def portfolio_cost(filename: str) -> float:
    """
    Calculates the cost of the portfolio by using the amount of shares
    and the corresponding price.

    :param filename: Name of the portfolio file
    :raises ValueError: Raises ValueError if type conversion cannot be done
    :return: The cost of the portfolio
    """
    total_cost = 0.0
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            if not row:
                continue
            try:
                rowdict = dict(zip(headers, row))
                total_cost += int(rowdict["shares"]) * float(rowdict["price"])

            except Exception:
                raise ValueError

    return total_cost
