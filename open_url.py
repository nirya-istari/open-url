#!/usr/bin/env python3
"""Open URL

Usage:
  open_url.py <file>

Options:
  -h --help     Show this screen.
  --version     Show version.
"""
from docopt import docopt
import configparser

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Open URL 1.0')
    print(arguments)

    
