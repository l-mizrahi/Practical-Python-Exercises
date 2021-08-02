import csv
from pathlib import Path
from typing import List, Tuple, Union, Callable, Dict


def parse_csv(
    file_path: Union[str, Path],
    select: List[str] = None,
    types: List[Callable] = None,
    has_headers: bool = True,
    delimiter: str = ",",
) -> List[Union[Dict, Tuple]]:
    """
    Parse a csv file into a list.

    :param file_path: Path to the csv file
    :param select: Columns to select
    :param types: List of types to convert each column
    :param has_headers: Indicator if file has headers.
                        If False, creates a list of tuples otherwise a list of dictionaries
    :param delimiter: Type of delimiter. Defaults to ','
    :return: List of items in the file
    """
    records: List[Union[Dict, Tuple]] = []
    record: Union[Dict, Tuple]
    indices: List[int] = []

    with open(file_path) as f:
        rows = csv.reader(f, delimiter=delimiter)
        if has_headers:
            headers = next(rows)
            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select

        for row in rows:
            if not row:
                continue
            if indices:
                row = [row[index] for index in indices]
            if types:
                row = [func(val) for func, val in zip(types, row)]

            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records
