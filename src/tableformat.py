from typing import List, Tuple
from abc import ABC, abstractmethod
import inspect
import sys


class TableFormatter(ABC):
    """
    Base class for formatting the portfolio report.
    This class should be extended to create tables in different formats.
    """

    @property
    @abstractmethod
    def fmt(self) -> str:
        """
        The name of the type of formatter, i.e. 'txt', 'csv', 'html', etc.
        """
        pass

    @abstractmethod
    def headings(self, headers: Tuple[str, str, str, str]) -> List[str]:
        """
        Format the table headings.

        :param headers: The headers of the table
        :return: The formatted headers
        """
        pass

    @abstractmethod
    def rows(self, rowdata: List[Tuple[str, int, float, float]]) -> List[str]:
        """
        Format rows of table data.

        :param rowdata: Rows of the table to be formatted
        :return: The formatted rows
        """
        pass

    def format(
        self,
        headers: Tuple[str, str, str, str],
        rows: List[Tuple[str, int, float, float]],
    ) -> List[str]:
        """
        Formats headers and rows as a table.
        :param headers: The headers of the table
        :param rows: Rows of the table to be formatted
        :raise ValueError: Raise error if headers or rows is empty,
                           or if the size of headers does not match the size of a row.
        :return: The formatted headers and rows
        """
        if not headers or not rows:
            raise ValueError("Headers or rows cannot be empty.")
        if len(headers) != max([len(row) for row in rows]):
            raise ValueError("Size of headers and rows must match")
        headings = self.headings(headers)
        row_list = self.rows(rows)
        return headings + row_list


class TextTableFormatter(TableFormatter):
    """
    Formats table in plain-text format.
    """

    fmt = "txt"

    def headings(self, headers: Tuple[str, str, str, str]) -> List[str]:
        """
        Format the table headings in text format.

        :param headers: The headers of the table
        :return: The formatted headers
        """
        fmt_str = " ".join(["{:>10s}"] * len(headers))
        dashes = " ".join(["-" * 10] * len(headers))
        headers_cap = list(map(lambda x: x.capitalize(), headers))
        headers_fmt = fmt_str.format(*headers_cap)
        return [headers_fmt, dashes]

    def rows(self, rowdata: List[Tuple[str, int, float, float]]) -> List[str]:
        """
        Format rows of table data in text format.

        :param rowdata: Rows of the table to be formatted
        :return: The formatted rows
        """
        output: List[str] = []
        fmt_str = " ".join(["{:>10s}"] * len(rowdata[0]))
        for row in rowdata:
            rowstr = [str(r) for r in row]
            output.append(fmt_str.format(*rowstr))
        return output


class CSVTableFormatter(TableFormatter):
    """
    Formats table in CSV format.
    """

    fmt = "csv"

    def headings(self, headers: Tuple[str, str, str, str]) -> List[str]:
        """
        Format the table headings in CSV format.

        :param headers: The headers of the table
        :return: The formatted headers
        """
        headers_cap = list(map(lambda x: x.capitalize(), headers))
        headers_str = [",".join(headers_cap)]
        return headers_str

    def rows(self, rowdata: List[Tuple[str, int, float, float]]) -> List[str]:
        """
        Format rows of table data in CSV format.

        :param rowdata: Rows of the table to be formatted
        :return: The formatted rows
        """
        output: List[str] = []
        for row in rowdata:
            rowstr = [str(r) for r in row]
            output.append(",".join(rowstr))
        return output


def is_formatter(x: object) -> bool:
    """
    Check if given object is a concrete Formatter object.

    :param x: Any Python object
    :return: True if x is a concrete formatter, False otherwise
    """
    return (
        inspect.isclass(x)
        and issubclass(x, TableFormatter)  # type: ignore
        and not inspect.isabstract(x)
    )


FORMAT2FORMATTER_CLS = {
    formatter_cls.fmt: formatter_cls
    for _, formatter_cls in inspect.getmembers(
        sys.modules[__name__], predicate=is_formatter
    )
}
