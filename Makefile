all: myanki

csv:
	libreoffice --headless --convert-to csv:"Text - txt - csv (StarCalc)":44,34,76 --outdir . words.ods

myanki: csv
	python3 csv_to_anki.py > words.myanki
