import csv
from pathlib import Path
from typing import List, Union, Callable


def parse_csv(
    file_path: Union[str, Path], select: List[str] = None, type: List[Callable] = None
) -> List[object]:
    """
    Parse a csv file into a list.

    :param file_path: Path to the csv file
    :param select: Columns to select
    :param type: List of types to convert each column
    :return: List of items in the file
    """
    records: List[object] = []
    with open(file_path) as f:
        rows = csv.reader(f)
        headers = next(rows)
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        for row in rows:
            if not row:
                continue
            if indices:
                row = [row[index] for index in indices]
            record = dict(zip(headers, row))
            records.append(record)

    return records
