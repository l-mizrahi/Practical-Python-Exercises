from typing import List, Tuple, Union, cast
import logging


class TableFormatter:
    """
    Base class for formatting the portfolio report.
    This class should be extended to create tables in different formats.
    """

    def headings(self, headers: Tuple[str, str, str, str]) -> List[str]:
        """
        Format the table headings.

        :param headers: The headers of the table
        :raises NotImplementedError: If headings() has not been overloaded
        :return: The formatted headers
        """
        raise NotImplementedError()

    def rows(self, rowdata: List[Tuple[str, int, float, float]]) -> List[str]:
        """
        Format a single row of table data.

        :param rowdata: A single row of the table to be formatted
        :raises NotImplementedError: If row() has not been overloaded
        :return: The formatted row
        """
        raise NotImplementedError()

    def format(
        self,
        data: Union[
            List[Tuple[str, str, str, str]], List[Tuple[str, int, float, float]]
        ],
    ) -> List[str]:
        """
        Formats data as a table.
        """
        if len(data) < 2:
            raise ValueError(
                f"Length of data is {len(data)}. data must have headers and at least one row"
            )
        headers = cast(Tuple[str, str, str, str], data[0])
        rows = cast(List[Tuple[str, int, float, float]], data[1:])
        headings = self.headings(headers)
        row_list = self.rows(rows)
        return headings + row_list


class TextTableFormatter(TableFormatter):
    """
    Formats table in plain-text format.
    """

    def headings(self, headers: Tuple[str, str, str, str]) -> List[str]:
        fmt_str = " ".join(["{:>10s}"] * len(headers))
        dashes = " ".join(["-" * 10] * len(headers))
        try:
            headers_cap = list(map(lambda x: x.capitalize(), headers))
            headers_fmt = fmt_str.format(*headers_cap)
        except ValueError:
            logging.exception(f"Couldn't convert headers to string: {headers}")
        return [headers_fmt, dashes]

    def rows(self, rowdata: List[Tuple[str, int, float, float]]) -> List[str]:
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

    def headings(self, headers: Tuple[str, str, str, str]) -> List[str]:
        headers_cap = list(map(lambda x: x.capitalize(), headers))
        return [",".join(headers_cap)]

    def rows(self, rowdata: List[Tuple[str, int, float, float]]) -> List[str]:
        output: List[str] = []
        for row in rowdata:
            rowstr = [str(r) for r in row]
            output.append(",".join(rowstr))
        return output
