'''
Created: Feb 21, 2017
Last Edited: Feb 22, 2017

@author: jes97210

This file handles the regex interpretations for strings. It searches over a
tree of possible comparisons. The comparisons themselves are stored in a text
file, so that if a new comparison needs to be made, it can be entered and
stored.
'''

import sys
import re

'''
The comparisons_regex.txt file
'''
comparison_file = "comparisons_regex.txt"
comparisons_dict = []
course_code = "[A-Z]{4}\s[0-9]{3}"

def open_comparison_file():
    f = open(comparison_file, "rU")
    f.close()

# Takes a string s
# Returns a string s (modified)
# Replaces "and" with "^", "or" with "v"
def replace(s):
    return True

def main():
    open_comparison_file()
