from typing import List, Tuple


class TableFormatter:
    """
    Base class for formatting the portfolio report.
    This class should be extended to create tables in different formats.
    """

    def headings(self, headers: Tuple[str, str, str, str]) -> List[str]:
        """
        Format the table headings.

        :param headers: The headers of the table
        :raises NotImplementedError: If headings() has not been overridden
        :return: The formatted headers
        """
        raise NotImplementedError()

    def rows(self, rowdata: List[Tuple[str, int, float, float]]) -> List[str]:
        """
        Format rows of table data.

        :param rowdata: Rows of the table to be formatted
        :raises NotImplementedError: If row() has not been overridden
        :return: The formatted rows
        """
        raise NotImplementedError()

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
