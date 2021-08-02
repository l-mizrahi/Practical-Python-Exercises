import csv
import logging
from pathlib import Path
from typing import Any, List, Tuple, Union, Callable, Dict, cast


def parse_csv(
    file_path: Union[str, Path],
    select: List[str] = None,
    types: List[Callable] = None,
    has_headers: bool = True,
    delimiter: str = ",",
    silence_errors=False,
) -> List[Any]:
    """
    Parse a csv file into a list.

    :param file_path: Path to the csv file
    :param select: Columns to select
    :param types: List of types to convert each column
    :param has_headers: Indicator if file has headers.
                        If False, creates a list of tuples otherwise a list of dictionaries
    :param delimiter: Type of delimiter. Defaults to ','
    :raises RuntimeError: Raises RuntimeError if both select and has_headers is False.
    :return: List of items in the file
    """
    if not has_headers and select:
        raise RuntimeError("select argument requires column headers")

    records: List[Any] = []
    indices: List[int] = []
    start: int = 0

    with open(file_path) as f:
        rows = csv.reader(f, delimiter=delimiter)
        if has_headers:
            headers = next(rows)
            start = 1
            records = cast(List[Dict], records)
            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select
        else:
            records = cast(List[Tuple], records)

        for rowno, row in enumerate(rows, start=start):
            if not row:
                continue
            if indices:
                row = [row[index] for index in indices]
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        logging.exception(f"Couldn't convert row {rowno}:{row}. {e}")
                    continue

            if has_headers:
                records.append(dict(zip(headers, row)))
            else:
                records.append(tuple(row))

    return records
