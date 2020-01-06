##################################################
# BfS Basics
##################################################

ifndef LIBREOFFICE_PATH
	ifeq ($(OS),Windows_NT)
		LIBREOFFICE_PATH = "C:\Program Files\LibreOffice\program\soffice"
	endif
endif

.PHONY: all clean

all: data/bfs/gwr-gbaups/ data/bfs/gwr-gheizs/ data/bfs/gwr-genhzs/

data/bfs/%/: build/ch/bfs/%.csv
	mkdir -p $(dir $@)
	python3 src/csv2dp.py -i "$<" -o "$@" -m "lib/$*.metadata.json"

build/ch/bfs/gwr-%.csv: build/ch/bfs/gwr.xlsx
	mkdir -p $(dir $@)
	python3 src/gwr.py -i "$<" -o "$@" -c "$*"

build/ch/bfs/gwr.xlsx: downloads/bfs/be-d-09.02-synopsis-02.xlsx
	mkdir -p $(dir $@)
	cp $<.download $@

downloads/bfs/be-d-09.02-synopsis-02.xlsx:
	mkdir -p $(dir $@)
	curl https://www.bfs.admin.ch/bfsstatic/dam/assets/7066269/master -L -o $@.download

clean:
	rm build/ch/bfs/gwr.csv
	rm build/ch/bfs/gwr.xlsx
	rm downloads/bfs/be-d-09.02-synopsis-02.xlsx