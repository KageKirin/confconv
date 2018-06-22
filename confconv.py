#! /usr/bin/python

import os, sys
import argparse, codecs
from pathlib import Path

import json, toml, toml, yaml, configparser, xmltodict
config = configparser.ConfigParser()
from ruamel.yaml import YAML
ry = YAML()

loader = {
    '.yaml' : yaml.load,
    '.json' : json.load,
    '.toml' : toml.load,
    '.ini'  : config.read_file,
    '.pyd'  : lambda f: eval(f.read()),
    '.xml'  : lambda f: xmltodict.parse(f.read(), process_namespaces=True)
}

def writeini(d, f):
    config.read_dict(d)
    config.write(f)

dumper = {
    '.yaml' : lambda d, f: f.write(yaml.dump(d)),
    '.json' : lambda d, f: f.write(json.dumps(d, sort_keys=True, indent=2)),
    '.toml' : lambda d, f: f.write(toml.dumps(d)),
    '.ini'  : lambda d, f: writeini(d,f),
    '.pyd'  : lambda d, f: f.write(str(d)),
    '.xml'  : lambda d, f: f.write(xmltodict.unparse(d, pretty=True))
}

def main(args):
    data = None
    with codecs.open(args.input, 'r', encoding='utf-8') as inputfile:
        data = loader[args.input_format](inputfile)

    print(data)

    with codecs.open(args.output, 'w', encoding='utf-8') as outputfile:
        dumper[args.output_format](data, outputfile)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='input file', type=Path)
    parser.add_argument('-o', '--output', help='output file', type=Path)
    parser.add_argument('-if', '--input-format', help='input format (overrides deduction by extension), supports: ' + ', '.join(loader.keys()))
    parser.add_argument('-of', '--output-format', help='output format (overrides deduction by extension), supports: ' + ', '.join(dumper.keys()))

    args = parser.parse_args()

    if not args.input_format:
        args.input_format = ''.join(args.input.suffixes)

    if not args.output_format:
        args.output_format = ''.join(args.output.suffixes)

    print(args)
    main(args)




