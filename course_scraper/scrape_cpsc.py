'''
Created: Feb 21, 2017
Last Edited: Feb 22, 2017

@author: jes97210

This script scrapes the computer science site, and lifts the required
information from the text.
References main_scrape.py and regex_comparisons.py
'''

import sys
import course_format
import main_scrape
import re
import regex_comparisons

cpsc_file = "cpsc_courses_raw.txt"
raw_courses = []
courses_list = []


def main():
    text = main_scrape.main()
    csfl = open(cpsc_file, "w")
    csfl.write(text)
    csfl.close()
    text = text.split('\n')
    temp = []
    for line in text:
        # Since this application is for undergrad UBC courses, don't store
        #  courses with a code greater than 4
        if line.startswith('CPSC 5') or line.startswith('CPSC 6'):
            if temp:
                raw_courses.append(temp)
            break
        elif line.startswith('CPSC'):
            if temp:
                raw_courses.append(temp)
            temp = [line]
        else:
            temp.append(line)
    # print(raw_courses)
    for c in raw_courses:
        try:
            temp = course_format.new_course(c)
        except IndexError as ie:
            print('For the following course:')
            print(c)
            print('The following error occured:')
            print(ie)
        except ValueError as ve:
            print('For the following course:')
            print(c)
            print('The following error occured:')
            print(ve)
        else:
            courses_list.append(temp)
    for course in courses_list:
        print(course.code)
    # print(courses_list)

if __name__ == "__main__":
    main()
