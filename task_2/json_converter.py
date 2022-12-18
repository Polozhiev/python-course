import csv
import json

class Converter:
    def __init__(self, data_csv, title=0, delimiter=','):
        self.title = data_csv[title]
        self.values = data_csv[0:title] + data_csv[title + 1:]
        self.delimiter = delimiter

    def prepare_title(self):
        title = self.title.strip().split(self.delimiter)
        return title

    def to_json(self):
        title = self.prepare_title()
        self.check_data(title)
        csvReader = csv.DictReader(self.values, fieldnames=title, delimiter=self.delimiter)
        res = [row for row in csvReader]
        jsonString = json.dumps(res, indent=4)
        return jsonString

    def check_data(self, title):
        values = [row.strip().split(self.delimiter) for row in self.values]
        len_title = len(title)
        for row in values:
            assert len_title == len(row), "Check input data"