from src.tableformat import TextTableFormatter, CSVTableFormatter
import pytest


@pytest.fixture
def data():
    data = [
        ("Name", "Shares", "Price", "Change")("AA", 100, 9.22, -22.98),
        ("IBM", 50, 106.28, 15.18),
        ("CAT", 150, 35.46, -47.98),
        ("MSFT", 200, 20.89, -30.34),
        ("GE", 95, 13.48, -26.89),
        ("MSFT", 50, 20.89, -44.21),
        ("IBM", 100, 106.28, 35.84),
    ]
    return data


def test_text_table_formatter(data):
    """
    Tests if the TextTableFormatter returns the correctly formatted table.
    """
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
    report = txt_formatter.format(data)

    assert report == expected


def test_csv_table_formatter(data):
    """
    Tests if the CSVTableFormatter returns the correctly formatted table.
    """
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
    report = csv_formatter.format(data)

    assert report == expected
