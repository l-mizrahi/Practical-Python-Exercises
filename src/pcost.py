import csv


def portfolio_cost(filename):
    total_cost = 0
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            if not row:
                raise ValueError
            total_cost += int(row[1]) * float(row[2])

    return total_cost
