#!/usr/bin/env python3
"""Sort BCOs
"""

import os
import json
import sys
import argparse

__version__ = "0.0.1"
__status__ = "BETA"

def usr_args():
    """User Arguments
    """

    parser = argparse.ArgumentParser()

    # set usages options
    parser = argparse.ArgumentParser(
        prog='bco',
        usage='%(prog)s [options]')

    # version
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='%(prog)s ' + __version__)

    parser.add_argument('-b', '--bco',
        required=True,
        help="path to BioCompute JSON file to process.")

    if len(sys.argv) <= 1:
        sys.argv.append('--help')

    options = parser.parse_args()
    return options
  
def load_bcos(bco:str):
    """Load BCOs
    """
    lines = open(bco, "r").read().split("\n")

    for line in lines:
        if line.strip() == "":
            continue
        bco_obj = json.loads(line)
        del bco_obj['_id']
        bco_id = 'OMX_' + bco_obj['bco_id'].split('/')[-1].split('_')[1]
        bco_obj['bco_id'] = 'http://data.oncomx.org/' + bco_id
        print(bco_obj['bco_id'])
        fileName = 'bcos/' + bco_id + '.json'
        print(fileName)
        with open(fileName, 'w+') as file:
            file.write(json.dumps(bco_obj, indent=4))

def main():
    """
    Main function
    """
    options = usr_args()
    load_bcos(options.bco)

if __name__ == "__main__":
    main()