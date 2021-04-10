import json
import pandas as pd
import os
import openpyxl
from utils.schema_check import create_schema
import csv


def read_data(path_to_data, path_to_schema, data_output, log_output):
    schema = create_schema(path_to_schema)
    wb = openpyxl.load_workbook(path_to_data)

    result = dict()
    errors = list()

    for r in schema:
        value = wb[r.sheet][r.location].value
        if r.is_valid_type(value):
            result[r.key] = value
        else:
            errors.append(f"{r.key}: Error reading value at sheet {r.sheet} cell {r.location}"
                          f". Expected {r.cell_type} but got {type(value)}")

    with open(log_output) as log_file:
        log_file.writelines(errors)


