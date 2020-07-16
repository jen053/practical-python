# fileparse.py
import csv


def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
    """
    Parse a CSV file into a list of  records
    """

    with open(filename) as f:

        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers
        headers = next(rows) if has_headers else []

        # If a column selector was given, fine indices of the specified column.
        # Also narrow the set of headers used for resulting dictionaries.
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []
        records = []
        for row in rows:
            if not row:
                continue  # Skip rows with no data
            # Filter the row if specific columns were selected
            if indices:
                row = [row[index] for index in indices]
            # Apply type conversion it types
            if types:
                row = [func(val) for func, val in zip(types, row)]
            # Create dictionary if headers, else contain rows within tuples
            if headers:
                record = dict(zip(headers, row))
            else:
                records = tuple(row)

            records.append(record)

    return records
