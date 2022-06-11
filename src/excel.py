import csv
from openpyxl import Workbook, load_workbook
import os


def get_csv(path: str = ''):
    if os.path.isfile(path):
        wb = load_workbook(path)
        ws = wb.active
        data = []
        keys = []

        for index, column in enumerate(ws):
            cell_data = []
            for cell in column:
                if index == 0:
                    keys.append(cell.value)
                else:
                    cell_data.append(cell.value)
            else:
                if cell_data:
                    data.append(cell_data)
        else:
            return csv_converter(path=path, keys=keys, data=data)
    else:
        return f'ERROR: FILE NOT FOUND: {path}'


def csv_converter(path: str, keys: list, data: list):
    path = list(os.path.splitext(path))
    path[1] = '.csv'
    path = ''.join(path)

    if isinstance(keys, list) and isinstance(data, list):
        with open(path, 'w', newline='') as file:
            writer = csv.writer(
                file,
                delimiter=',',
                quotechar='"',
                quoting=csv.QUOTE_ALL
            )

            writer.writerow(keys)

            for dt in data:
                writer.writerow(dt)

    return path
