import csv


def portfolio_cost(filename):
    total_cost = 0
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            if not row:
                continue
            try:
                row = dict(zip(headers, row))
                total_cost += int(row["shares"]) * float(row["price"])

            except Exception:
                raise ValueError

    return total_cost
