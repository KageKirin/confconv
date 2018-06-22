#! /usr/bin/python

import os, sys
import argparse, codecs
from pathlib import Path

import json, toml, toml, yaml #, config, yaml
from ruamel.yaml import YAML
ry = YAML()

loader = {
    
    '.yaml' : yaml.load,
    '.json' : json.load,
    '.toml' : toml.load,
    #'ini'  : config.load
}

dumper = {
    '.yaml' : yaml.dump,
    '.json' : json.dumps,
    '.toml' : toml.dumps,
    #'ini'  : config.dumps
}

def main(args):
    data = None
    with codecs.open(args.input, 'r', encoding='utf-8') as inputfile:
        data = loader[args.input_format](inputfile)

    print(data)

    with codecs.open(args.output, 'w', encoding='utf-8') as outputfile:
        d = dumper[args.output_format]
        outputfile.write(d(data))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='input file', type=Path)
    parser.add_argument('-o', '--output', help='output file', type=Path)
    parser.add_argument('-if', '--input-format', help='input format (overrides deduction by extension)')
    parser.add_argument('-of', '--output-format', help='output format (overrides deduction by extension)')

    args = parser.parse_args()

    if not args.input_format:
        args.input_format = ''.join(args.input.suffixes)

    if not args.output_format:
        args.output_format = ''.join(args.output.suffixes)

    print(args)
    main(args)




