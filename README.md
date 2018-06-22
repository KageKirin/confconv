# confconv

Configuration converter

## Why?

Ever had to convert config files from YAML to JSON to TOML?
This tool should be able to handle it.

## How?

Python loads config files as `dict`, and those dicts can be written again in a different format.

## More?

I'll add more formats as I see fit or as I need.

## Caveats?

Not all formats are born equal. In fact, some formats have limitations as to their contents.
- XML can only have 1 root element
- JSON can have an array `[]` as root element, although not all parsers support this
- TOML and INI do not support having arrays as root, so converting from YAML might fail.

## Supported formats?

Following formats are supported so far, as far as their respective parsers go:
- YAML
- JSON
- TOML
- INI (via Python ConfigParser)
- PYD (Python Data): dump from Python, read back through `eval()`.
- XML (via Python xmltodict)
