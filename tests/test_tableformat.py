from src.tableformat import TextTableFormatter, CSVTableFormatter
import pytest


@pytest.fixture
def data():
    headers = ("Name", "Shares", "Price", "Change")
    rows = [
        ("AA", 100, 9.22, -22.98),
        ("IBM", 50, 106.28, 15.18),
        ("CAT", 150, 35.46, -47.98),
        ("MSFT", 200, 20.89, -30.34),
        ("GE", 95, 13.48, -26.89),
        ("MSFT", 50, 20.89, -44.21),
        ("IBM", 100, 106.28, 35.84),
    ]
    return headers, rows


def test_text_table_formatter(data):
    """
    Tests if the TextTableFormatter returns the correctly formatted table.
    """
    headers, rows = data
    expected = [
        "      Name     Shares      Price     Change",
        "---------- ---------- ---------- ----------",
        "        AA        100       9.22     -22.98",
        "       IBM         50     106.28      15.18",
        "       CAT        150      35.46     -47.98",
        "      MSFT        200      20.89     -30.34",
        "        GE         95      13.48     -26.89",
        "      MSFT         50      20.89     -44.21",
        "       IBM        100     106.28      35.84",
    ]
    txt_formatter = TextTableFormatter()
    print(headers, rows)
    report = txt_formatter.format(headers, rows)

    assert report == expected


def test_csv_table_formatter(data):
    """
    Tests if the CSVTableFormatter returns the correctly formatted table.
    """
    headers, rows = data
    expected = [
        "Name,Shares,Price,Change",
        "AA,100,9.22,-22.98",
        "IBM,50,106.28,15.18",
        "CAT,150,35.46,-47.98",
        "MSFT,200,20.89,-30.34",
        "GE,95,13.48,-26.89",
        "MSFT,50,20.89,-44.21",
        "IBM,100,106.28,35.84",
    ]
    csv_formatter = CSVTableFormatter()
    report = csv_formatter.format(headers, rows)

    assert report == expected


def test_table_formatter_no_data_or_headers():
    """
    Test if TableFormatter raises a ValueError if headers or rows is empty.
    """
    txt_formatter = TextTableFormatter()
    with pytest.raises(ValueError):
        txt_formatter.format(("Name", "Shares", "Price", "Change"), [()])

    with pytest.raises(ValueError):
        txt_formatter.format((), [("AA", 100, 9.22, -22.98)])


def test_table_formatter_size_of_headers_rows():
    """
    Tests if TableFormatter raises a ValueError if size of headers doesn't match size of a row.
    """
    txt_formatter = TextTableFormatter()
    with pytest.raises(ValueError):
        txt_formatter.format(("Name", "Shares", "Price"), [("AA", 100, 9.22, -22.98)])

    with pytest.raises(ValueError):
        txt_formatter.format(("Name", "Shares", "Price", "Change"), [("AA", 100, 9.22)])
