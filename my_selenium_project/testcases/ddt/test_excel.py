import pytest
import xlrd


def get_data():
    filename = 'data.xlsx'
    wb = xlrd.open_workbook(filename)
    sheet = wb.sheet_by_index(0)
    rows = sheet.nrows
    cols = sheet.ncols
    lst = []
    for row in range(rows):
        for col in range(cols):
            cell_data = sheet.cell_value(row, col)
            lst.append(cell_data)

    return lst


@pytest.mark.parametrize('name', get_data())
def test1(name):
    print(name)


if __name__ == '__main__':
    pytest.main(['-sv', 'test_excel.py'])
