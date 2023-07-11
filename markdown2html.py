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
import re
import hashlib


def convert_markdown_to_html(input_file, output_file):
    # Read the content of the Markdown file
    with open(input_file, 'r') as file:
        markdown_content = file.read()

    # Convert Markdown headings to HTML
    markdown_content = re.sub(r'^(#+)(.*)', convert_heading, markdown_content, flags=re.MULTILINE)

    # Convert Markdown unordered lists to HTML
    markdown_content = re.sub(r'^\s*-\s+(.*)', r'<li>\1</li>', markdown_content, flags=re.MULTILINE)
    markdown_content = f'<ul>{markdown_content}</ul>'

    # Convert Markdown ordered lists to HTML
    markdown_content = re.sub(r'^\s*\*\s+(.*)', r'<li>\1</li>', markdown_content, flags=re.MULTILINE)
    markdown_content = f'<ol>{markdown_content}</ol>'

    # Convert Markdown paragraphs to HTML
    markdown_content = re.sub(r'^([^#\-\*\n\r].*)', r'<p>\1</p>', markdown_content, flags=re.MULTILINE)
    markdown_content = re.sub(r'\n', r'<br />\n', markdown_content)

    # Convert bold syntax to HTML
    markdown_content = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', markdown_content)

    # Convert additional syntax for generating HTML
    markdown_content = re.sub(r'\[\[(.*?)\]\]', lambda match: hashlib.md5(match.group(1).encode()).hexdigest(), markdown_content)
    markdown_content = re.sub(r'\(\((.*?)\)\)', lambda match: match.group(1).replace('c', '').replace('C', ''), markdown_content, flags=re.IGNORECASE)

    # Write the HTML content to the output file
    with open(output_file, 'w') as file:
        file.write(markdown_content)


def convert_heading(match):
    heading_level = len(match.group(1))
    heading_text = match.group(2).strip()
    html_heading = f"<h{heading_level}>{heading_text}</h{heading_level}>"
    return html_heading


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

