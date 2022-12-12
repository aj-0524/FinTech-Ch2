# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def outputcsv(file_location, qualifying_loans):
    # Made a header for the CSV file, should the user choose to download it.
    header = 'Financial Institution', 'Maximum Loan Amount', 'Maximum Loan:Value', 'Maximum Debt:Income', 'Minimum Credit Score', 'Interest Rate'
    csvpath = Path(file_location)
    print(f'Saving list of qualifying loans to...{csvpath}')
    # This is where the qualifyting loans and header will be written to a CSV file in the location they inputted.
    with open(csvpath, 'w', newline= '') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(header)
        for row in qualifying_loans:
            csvwriter.writerow(row)
    return
