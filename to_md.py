#!/usr/bin/env python3

# to_md.py

###############
# A script to convert from a tsv of source language
# and target language translations
#
# Written by Coleman Donaldson for the 
# [Ajami Lab](https://www.manuscript-cultures.uni-hamburg.de/ajami/index_e.html)
#
# The main use of this script is to convert a TSV file
# [exported from a Tropy project](https://zenodo.org/record/2581225)
# into a plain text prose format
# using the conventions of
# [Markdown](https://daringfireball.net/projects/markdown/)
#
# Once in plain text markdown, you can use Pandoc flavored markdown to
# write a critical edition style text with footnotes etc., for publications
#
##############


#########################
# FUTURE FEATURES TO ADD:
# 
# The ability to change [Ajami Lab Tropy text conventions](https://zenodo.org/record/2581217)
# to basic markdown formatting (for italics and code) that is useful for publication
# 
# For future reference, this standard is as follows:
# Arabic	Ajami	<Transliteration in angle brackets>	Phonemic	‘Transliteration in smart single quotes’
#
#########################

help_text = """
Convert a tsv file of source language segments and corresponding
interpretation and translation segments into a markdown file

Usage:

    to_md filename

    filename: the input tsv file to process

    Example:

        to_md manuscript.tsv

input file notes:
    - The input file must be a tab-separated value file
    - The first row must be a series of headers
    - The first column must be identifiers for the segments

outout file notes:
    - Identifiers become markdown headers via three hashtag marks
    - Language segments become markdown paragraphs
"""

import os, re, sys

######
#
# Check if we are running at least Python 3, if not exit with an error
#
#####

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

#####
#
# Check if --help was requested
#
#####

if len(sys.argv) == 2 and sys.argv[1] == "--help":
    print(help_text)
    sys.exit()

########
#
# Handle command line arguments
#
########

# Save the filename by popping it off what was input via the command line
filename = sys.argv.pop()

#########
#
# Functions
#
#########


# Abstract away saving the file so we can handle it by itself
# We want to save the processed file in the same directory as the input file
# so we must take that as an argument
def save_to_file(data, input_filename):
    contents = data
    # Get the directory and filename from the input filename
    (directory, file_and_ext) = os.path.split(input_filename)
    # Get the filename minus the extension (.tsv)
    (output_filename, _) = os.path.splitext(file_and_ext)
    # Build the new complete file name to save to
    output_filename = os.path.join(directory, output_filename + ".md")
    # If that file already exists we need to ask to override it
    if os.path.exists(output_filename):
        response = input("The file " + output_filename + " already exists. Overwrite? y/n \n")
        if response.lower() == 'y':
            # If they responded y then write the file 
            do_write_file(contents, output_filename)
        else:
            # If they responded anything else exit
            print("Did not write the file")
    else:
      # If the file doesn't already exist then write the file
      do_write_file(contents, output_filename)

#####
# File writing
#####

def do_write_file(contents, output_filename):
    with open(output_filename, 'w') as file:
        file.write(contents)
        print("Wrote MD to: ", output_filename)

########
#
# Script
#
########

# Create buffer for output
output = ""

# Store which line number we're working on for good error reporting
line_number = 0

# Store whether we are looking at an ID column or not
isID = 1

# Store whether the markdown file has poundsigns for identifier as a header
hasPounds = 0

# Open the file for reading
with open(filename, 'r') as inputFile:
    
    # Loop through the lines
    for line in inputFile:
        
        # Increment the current line number for error reporting    
        line_number += 1
        # Ignore the first line since it is the TSV headers
        if line_number == 1:
            continue
                
        # Otherwise process the lines
        else:
            
            # Split the line on the tab character to build a list of the columns
            split_line = line.split('\t')
            
            # If the split line is less than two items
            if len(split_line) < 2:
                # Raise an error since that means there's not enough columns
                raise Exception("Line " + line_number + " doesn't have enough columns.")
            
            # Write the markdown header
            output += "### " + split_line[0] + "\n\n"
            
            # Write the language lines. The last one needs one less new line.
            for lang in split_line[1:-1]:
                output += lang + "\n\n"
            for lang in split_line[-1:]:
                output += lang + "\n"
                    
    # Try to save the file
    save_to_file(output, filename)