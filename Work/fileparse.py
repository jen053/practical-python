# fileparse.py
import csv


# Exercise 3.3
def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
    """
    Parse a CSV file into a list of  records
    """

    with open(filename) as f:
        # Exercise 3.7
        rows = csv.reader(f, delimiter=delimiter)

        # Exercise 3.6
        # Read the file headers
        headers = next(rows) if has_headers else []

        # Exercise 3.4
        # If a column selector was given, fine indices of the specified column.
        # Also narrow the set of headers used for resulting dictionaries.
        if select:
            if not has_headers:
                # Exercise 3.8
                raise RuntimeError('To select columns, file must have headers.')
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

            # Exercise 3.5
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
