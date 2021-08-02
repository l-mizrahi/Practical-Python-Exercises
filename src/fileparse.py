import csv
from pathlib import Path
from src.report import PortDict
from typing import List, Union


def parse_csv(file_path: Union[str, Path]) -> List[PortDict]:
    """
    Parse a csv file into a list.

    :param file_path: Path to the csv file
    :return: List of items in the file
    """
    records: List[PortDict] = []
    with open(file_path) as f:
        rows = csv.reader(f)
        next(rows)
        for name, shares, price in rows:
            if not all([name, shares, price]):
                continue
            pdict = PortDict(name=name, shares=int(shares), price=float(price))
            records.append(pdict)

    return records
