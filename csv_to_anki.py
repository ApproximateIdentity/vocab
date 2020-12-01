#!/usr/bin/env python3

import csv

def format_row(row, first_lang='english'):
    # Initial data cleaning
    row = {key: val.strip() for key, val in row.items()}
    # Sanity checks
    assert first_lang in ['english', 'czech']
    assert row['type'] in ['adj', 'adv', 'noun', 'verb']
    # Formatting
    second_lang = 'czech' if first_lang == 'english' else 'english'
    if row['type'] == 'adj':
        return f"{row[first_lang]};{row[second_lang]}"       
    elif row['type'] == 'noun':
        assert row['gender'] in ['m', 'f', 'n']
        return f"{row[first_lang]};{row[second_lang]} ({row['gender']})"
    elif row['type'] == 'adv':
        if first_lang == 'english':
            return f"{row[first_lang]} ({row['type']});{row[second_lang]}"
        else:
            return f"{row[second_lang]};{row[second_lang]} ({row['type']})"
    else:
        raise NotImplementedError(f"row type: {row['type']}")

for row in csv.DictReader(open('words.csv')):
    print(format_row(row, first_lang='english'))
    print(format_row(row, first_lang='czech'))
