import csv


def create_schema(path):
    data = list()
    with open(path, newline='') as file:
        reader = csv.reader(file, delimiter=',', quotechar='\"')
        for row in reader:
            data.append(row)
    raw_schema = list(map(row_to_schema, data[1:]))
    return raw_schema


def row_to_schema(row):
    return SchemaRow(key=row[0], sheet=row[1], location=row[2], cell_type=row[3])


class SchemaRow:
    def __init__(self, key, sheet, location, cell_type):
        self.key = key
        self.sheet = sheet
        self.location = location
        self.cell_type = cell_type

    def is_valid_type(self, value):
        return isinstance(value, self.get_type())

    def get_type(self):
        if self.cell_type == "STRING":
            return str
        if self.cell_type == "INTEGER":
            return int
        if self.cell_type == "DECIMAL":
            return float
        if self.cell_type == "BOOLEAN":
            return bool
