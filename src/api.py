from src import excel


def main(path=''):
    csv_path = excel.get_csv(path)
    return csv_path
