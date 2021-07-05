# Python 3.7
# File name: 
# Description: 
# Authors: Aaron Watt
# Date: 2021-06-26

# Standard library imports

# Third-party imports

# Local application imports

# FUNCTIONS --------------------------
def csv_to_dict(csv_path):
    import csv
    with open(csv_path, mode='r') as infile:
        reader = csv.reader(infile)
        rows = [row for row in reader]
        if len(rows[0])>2:  # dict of dicts
            headers = rows.pop(0)
            mydict = {row[0]:{headers[i]: row[i] for i in range(len(headers))} for row in rows}
        else:  # simple dict
            mydict = {row[0]: row[1] for row in rows}
    return mydict


def csv_to_nparrays(csv_path):
    pass

# MAIN -------------------------------
if __name__ == "__main__":
    pass

# REFERENCES -------------------------
"""

"""
