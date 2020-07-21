# fileparse.py
import csv


# Exercise 3.3
def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', show_errors=False):
    """
    Parse a CSV file into a list of  records
    """

    # Exercise 3.7; 3.17
    rows = csv.reader(lines, delimiter=delimiter)

    # Exercise 3.6
    # Read the file headers
    headers = next(rows) if has_headers else []

    # Exercise 3.4
    # If a column selector was given, fine indices of the specified column.
    # Also narrow the set of headers used for resulting dictionaries.
    if select:
        # Exercise 3.8
        if not has_headers:
            raise RuntimeError('To select columns, file must have headers.')
        indices = [headers.index(colname) for colname in select]
        headers = select

    records = []
    for ronum, row in enumerate(rows, 1):
        if not row:
            continue  # Skip rows with no data
        # Filter the row if specific columns were selected
        if select:
            row = [row[index] for index in indices]

        # Exercise 3.5
        # Apply type conversion it types
        if types:
            # Exercise 3.9 - 3.10
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not show_errors:
                    print(f" Row {ronum}: couldn't convert {row}")
                    print(f" Row {ronum}: reason {e}")
                continue

        # Create dictionary if headers, else contain rows within tuples
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)

        records.append(record)

    return records
