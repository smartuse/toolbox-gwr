# Swiss GWR data structure descriptions

> This is part of a statistical and geodata toolbox developed by SmartUse GmbH to make work with statistical and geographical data frictionless and accessible.

## Getting started

To get started, clone this repository.

    git clone git@github.com:smartuse/toolbox-gwr.git
    cd toolbox-gwr/

To generate the datapackages with csv based definitions by the Swiss Federal Office for Statitics on `Building Periods`, `Heating` and `Energy source` you need Python 3.7 as well as `dataflows`, `lxml` and `pandas`. To install run

    pip3 install dataflows lxml pandas

or 

    pip3 install -r requirements.txt

To finally generate the files simply run

    make

`make` and `make all` will generate:

* `data/bfs/gwr-gbaups` (Building periods)
* `data/bfs/gwr-genhzs` (Heating energy source)
* `data/bfs/gwr-gheizs` (Heating type)

## Copyright and License

### Author

Thorben Westerhuys, [SmartUse GmbH](https://smartuse.ch)

### Data Source

Data source is the Swiss Federal Office of Statistics, [GWS](https://www.bfs.admin.ch/bfs/de/home/statistiken/bau-wohnungswesen/erhebungen/gws2009.assetdetail.7066269.html), 2009.

### License

This package is licensed by its maintainers under the Public Domain Dedication and License.

If you intended to use these data in a public or commercial product, please check the data sources themselves for any specific restrictions.