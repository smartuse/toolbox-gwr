#!/usr/bin/python

import argparse, sys

from dataflows import Flow, load, update_package, printer, dump_to_path
import io
import json
import requests
import lxml.html

def parseExtraMetadata(path):

    # Supported datafields 
    data = dict(
        name="",
        title="",
        license="",
        licenses=[],
        sources=[],
        contributors=[],
        maintainers=[]
    )

    if path != None:
        with io.open(path, mode="r", encoding="utf-8") as json_file:
            metadata = json.load(json_file)

        if metadata["name"] != None:
            data["name"] = metadata["name"]
        
        if metadata["title"] != None:
            data["title"] = metadata["title"]
        
        if metadata["contributors"] != None:
            data["contributors"] = metadata["contributors"]
        
        if metadata["maintainers"] != None:
            data["maintainers"] = metadata["maintainers"]
        
        if metadata["sources"] != None:
            for sourceUrl in metadata["sources"]:
                doc = lxml.html.fromstring(requests.get(sourceUrl).content)
                webTitle = doc.xpath('//title')[0].text
                data["sources"].append(dict(title=webTitle,url=sourceUrl))
        
        if metadata["licenses"] != None:
            for license in metadata["licenses"]:
                if license == "PDDL-1.0":
                    licenseType = "ODC-PDDL-1.0"
                    licenseUrl = "http://opendatacommons.org/licenses/pddl/1.0/"
                data["licenses"].append(dict(type=licenseType,url=licenseUrl))
                data["license"] = data["licenses"][0]["type"]
        
    return data

def main():
    parser=argparse.ArgumentParser()

    parser.add_argument('-i', help='Path to CSV [CSV]')
    parser.add_argument('-o', help='Path to Output Directory [DIR]')
    parser.add_argument('-m', help='Merge this metadata (Author, License, ...) [JSON]')

    args=parser.parse_args()

    # Load additional metadata if any
    addedMetadata = parseExtraMetadata(args.m)
    # print(addedMetadata)

    # Load with Dataflows and save back as DataPackage
    Flow(
        load(args.i),
        update_package(title=addedMetadata["title"]),
        update_package(name=addedMetadata["name"]),
        update_package(license=addedMetadata["license"]),
        update_package(licenses=addedMetadata["licenses"]),
        update_package(contributors=addedMetadata["contributors"]),
        update_package(maintainers=addedMetadata["maintainers"]),
        update_package(sources=addedMetadata["sources"]),
        dump_to_path(args.o)
    ).process()

if __name__ == "__main__":
    main()