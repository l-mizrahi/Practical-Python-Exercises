import csv


def portfolio_cost(filename: str) -> float:
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
