#!/usr/bin/python

import argparse, sys

import pandas as pd

def main():

    parser=argparse.ArgumentParser()

    parser.add_argument('-i', help='Path to Excel File')
    parser.add_argument('-o', help='Path to Output File, defaults to input as .csv')
    parser.add_argument('-c', help='Column to parse from GWR file')

    args=parser.parse_args()

    gwr = pd.read_excel(args.i, header=1)
    # print(gwr.head())

    val = gwr.loc[gwr["Feldname"] == args.c.upper()]["Wert"].values[0].split("\n")
    lab = gwr.loc[gwr["Feldname"] == args.c.upper()]["Bezeichnungen"].values[0].split("\n")

    gwr_list = pd.DataFrame(dict(values=val,labels=lab))
    gwr_list = gwr_list.set_index("values")
    # print(gwr_list)

    gwr_list.to_csv(args.o)

if __name__ == "__main__":
    main()