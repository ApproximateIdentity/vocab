all: myanki

csv:
	libreoffice --headless --convert-to csv:"Text - txt - csv (StarCalc)":44,34,76 --outdir . news.ods

myanki: csv
	python3 csv_to_anki.py > news.myanki

clean:
	rm -fv *.csv *.myanki
