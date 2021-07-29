import csv


def portfolio_cost(file_path: str) -> float:
    """
    Calculates the cost of the portfolio by using the amount of shares
    and the corresponding price.

    :param file_path: Path to the portfolio file
    :raises ValueError: Raises error if a 'shares' value cannot be converted to an int
                        or if a 'price' value cannot be converted to a float
    :return: The cost of the portfolio
    """
    total_cost = 0.0
    with open(file_path) as f:
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
