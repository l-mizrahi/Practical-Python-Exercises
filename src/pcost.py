import csv


def portfolio_cost(file_path: str) -> float:
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
                print(f"Row {rowno}: Bad row {rowdict}")

    return total_cost
