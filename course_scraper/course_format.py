'''
Created: Feb 22, 2017

@author: jes97210

This file provides a "course format", a general structure that all courses on
the UBC site share. They typically have a course code, credits, title, and
desription. They can also have prereqs, equivalents, and coreqs.
This file also provides some simple methods.
'''

import sys
import re

course_code = re.compile("[A-Z]{4}\s[0-9]{3}")
course_credit = re.compile("\(\d\)")


class Course:

    def __init__(self, code, credits, title, desc, prq, equ, corq):
        self.code = code
        self.credits = credits
        self.title = title
        self.desc = desc
        self.prq = prq
        self.equ = equ
        self.corq = corq

'''
This takes an array of strings, and makes a new Course object.
Takes: Arr ([String])
    ASSUMES: len(Arr) >= 2
    First entry in Arr has the course code, credits, and title
    Second entry has course description
    Subsequent entries may have prereqs, equivalents, and/or coreqs
Returns: a Course object
'''
def new_course(Arr):
    a = Arr[0]
    b = Arr[1]
    c = Arr[2:]

    # Processing a
    # Typically: 'course_code course_credit title'
    a.strip()
    a1 = course_code.match(a)
    if a1 is None:
        raise IndexError('No course code found!')
    a2 = course_credit.search(a)
    if a2 is None:
        a2 = "3"  # default if nothing found
        print('No course credit found for: ' + a1.group())
        a3 = a[a1.end():]
        a3.strip()
    else:
        a3 = a[a2.end():]
        a3.strip()
        a2 = a2.group()

    a1 = a1.group()
    a1 = a1.replace(" ", "")

    # Processing b
    # Basically nothing needed
    b.strip()

    # Processing c
    c1 = None     # Prerequisite
    c2 = None   # Equivalency
    c3 = None     # Corequisite
    for i in c:
        if i.startswith('Prerequisite:'):
            c1 = i.replace('Prerequisite:', '', 1).strip()
        elif i.startswith('Corequisite:'):
            c2 = i.replace('Corequisite:', '', 1).strip()
        elif i.startswith('Equivalency:'):
            c3 = i.replace('Equivalency:', '', 1).strip()
        else:
            raise ValueError('Unexpected string: ' + i)

    # Make the Course instance
    return Course(a1, a2, a3, b, c1, c2, c3)
