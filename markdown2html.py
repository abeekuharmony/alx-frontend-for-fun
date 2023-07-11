#!/usr/bin/python3

"""
markdown2html.py - A script to convert Markdown files to HTML.

Usage: markdown2html.py <input_file> <output_file>

Arguments:
    <input_file>    : Name of the Markdown file to convert.
    <output_file>   : Name of the HTML file to output.

Requirements:
    - The number of arguments should be 2.
    - The Markdown file should exist.
    - PEP 8 style (version 1.7.*).
    - The code should not be executed when imported.
"""

import sys
import os.path


def convert_markdown_to_html(input_file, output_file):
    # Perform the conversion here (replace with your actual code)
    print(f"Converting {input_file} to {output_file}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py <input_file> <output_file>\n")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)

    convert_markdown_to_html(input_file, output_file)

    sys.exit(0)

