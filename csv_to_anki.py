#!/usr/bin/env python3

import csv

def formatter(dict_reader):
    for row in dict_reader:
        # Initial data cleaning
        row = {key: val.strip() for key, val in row.items()}
        # Sanity checks
        assert row['type'] in ['adj', 'adv', 'noun', 'verb', 'phrase', 'prep', 'conj', 'pron', 'comp', 'interj']
        # Formatting
        for first_lang in ['english', 'czech']:
            second_lang = 'czech' if first_lang == 'english' else 'english'
            if row['type'] == 'adj':
                yield f"{row[first_lang]};{row[second_lang]}"
            elif row['type'] == 'noun':
                assert row['gender'] in ['m', 'f', 'n']
                pronoun = {'m': 'ten', 'f': 'ta', 'n': 'to'}[row['gender']]
                if first_lang == 'english':
                    yield f"{row[first_lang]};{pronoun} {row[second_lang]}"
                else:
                    yield f"{pronoun} {row[first_lang]};{row[second_lang]}"
            elif row['type'] in ['adv', 'conj', 'pron']:
                if first_lang == 'english':
                    yield f"{row[first_lang]} ({row['type']});{row[second_lang]}"
                else:
                    yield f"{row[first_lang]};{row[second_lang]} ({row['type']})"
            elif row['type'] == 'prep':
                # XXX - Temporarilly removing prepositions to make them better...
                pass
            elif row['type'] == 'verb':
                perfective = row["perfective"]
                if perfective:
                    perfective = "." + perfective
                yield f"{row[first_lang]} (v{perfective});{row[second_lang]}"
            elif row['type'] in ['phrase', 'comp', 'interj']:
                yield f"{row[first_lang]};{row[second_lang]}"
            else:
                raise NotImplementedError(f"row type: {row['type']}")

for row in formatter(csv.DictReader(open('words.csv'))):
    print(row)
