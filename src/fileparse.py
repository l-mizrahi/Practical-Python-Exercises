import csv
import logging
from pathlib import Path
from typing import Any, List, TextIO, Union, Dict


def parse_csv(
    file_path_or_buffer: Union[str, Path, TextIO],
    select: List[str] = None,
    convert_fn: Any = None,  # Using Union[List[Callable], Dict[str, Callable]] breaks everything :(
    has_headers: bool = True,
    delimiter: str = ",",
    verbose: bool = True,
) -> Union[List[tuple], List[Dict[str, Any]]]:
    """
    Parse a csv file into a list.

    :param file_path_or_buffer: Path to the csv file or file-like object
    :param select: Columns to select
    :param convert_fn: List or dictionary of functions to apply to each column
    :param has_headers: Indicator if file has headers.
                        If False, creates a list of tuples otherwise a list of dictionaries
    :param delimiter: Type of delimiter. Defaults to ','
    :param verbose: Indicates if errors should be logged
    :raises RuntimeError: Raises RuntimeError if arguments are not compatible with each other.
                          If select is given then has_headers must be True.
                          Keys in convert_fn must be the same values in select.
                          If there are headers then convert_fn must be a dict of col_name:type.
                          Keys in convert_fn must match the name of the headers.
    :return: List of items in the file
    """

    if not has_headers and select:
        raise RuntimeError("'select' argument requires column headers")
    if (
        select
        and convert_fn
        and isinstance(convert_fn, dict)
        and set(select) != set(convert_fn.keys())
    ):
        raise RuntimeError("keys of 'convert_fn' must be the same as 'select'")
    if has_headers and convert_fn and not isinstance(convert_fn, dict):
        raise RuntimeError(
            "if 'has_headers' is True then 'convert_fn' must be a dictionary of col_name:type"
        )

    records: List[Any] = []
    indices: List[int] = []
    start: int = 0
    file_is_path = False

    if isinstance(file_path_or_buffer, (str, Path)):
        file_is_path = True
        file_path_or_buffer = open(file_path_or_buffer)

    rows = csv.reader(file_path_or_buffer, delimiter=delimiter)
    if has_headers:
        headers = next(rows)
        if (
            convert_fn
            and not select
            and isinstance(convert_fn, dict)
            and set(headers) != set(convert_fn.keys())
        ):
            raise RuntimeError("keys of 'convert_fn' does not match keys in headers")
        start = 1
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select

    for rowno, row in enumerate(rows, start=start):
        if not row:
            continue
        if indices:
            row = [row[index] for index in indices]

        if has_headers:
            rowdict = dict(zip(headers, row))
            if convert_fn:
                try:
                    rowdict = {
                        key: func(rowdict[key]) for key, func in convert_fn.items()
                    }
                except ValueError:
                    if verbose:
                        logging.exception(f"Couldn't convert row {rowno}:{row}")
                    continue
            records.append(rowdict)

        else:
            if convert_fn:
                try:
                    row = [func(val) for func, val in zip(convert_fn, row)]
                except ValueError:
                    if verbose:
                        logging.exception(f"Couldn't convert row {rowno}:{row}")
                    continue
            records.append(tuple(row))

    if file_is_path:
        file_path_or_buffer.close()

    return records
