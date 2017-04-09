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
import psycopg2

import re
import regex_comparisons

cpsc_file = "cpsc_courses_raw.txt"
raw_courses = []
course_list = []
leadto_dict = {}  # map: courseID -> set(courseID). To be populated as scraping goes on, then used on DB
conn = psycopg2.connect(
    dbname="dbj5dke7k2llc2",
    user="tkybpgvuevmgyp",
    password="fce7442d8e5a39771caae45610673a14ff60325a71ed5170748e2f5bd7c95d79",
    host="ec2-23-21-220-167.compute-1.amazonaws.com",
    port="5432"
)


def main():
    delete_table_contents()
    scrape_site("CPSC")
    populate_leadto_dict()
    populate_database()


def scrape_site(dept_code):
    text = main_scrape.main(dept_code)
    # csfl = open(cpsc_file, "w")
    # csfl.write(text)
    # csfl.close()
    text = text.split('\n')
    temp = []
    for line in text:
        # Since this application is for undergrad UBC courses, don't store
        #  courses with a code greater than 4
        if line.startswith(dept_code + ' 5') or line.startswith(dept_code + ' 6'):
            if temp:
                raw_courses.append(temp)
            break
        elif line.startswith(dept_code):
            if temp:
                raw_courses.append(temp)
            temp = [line]
        else:
            temp.append(line)
    # print(raw_courses)
    for c in raw_courses:
        try:
            new_course = course_format.new_course(c)
        except IndexError as ie:
            print('For the following course:')
            print(c)
            print('The following error occurred:')
            print(ie)
        except ValueError as ve:
            print('For the following course:')
            print(c)
            print('The following error occurred:')
            print(ve)
        else:
            # add the course to the list, and check if it already exists in leadto_dict
            course_list.append(new_course)

            if new_course.code not in leadto_dict:
                # add the newly seen code with an empty list to be populated
                leadto_dict[new_course.code] = set()

    # for course in courses_list:
    #     print(course.equ)


def populate_leadto_dict():
    for course in course_list:
        prereq_list = desc_to_list(course.prq)
        if prereq_list is not None:
            for prereq in prereq_list:
                if prereq in leadto_dict:
                    # for each prereq in each course, add the course to the dictionary
                    # as a 'leadto' for that specific prereq
                    leadto_dict[prereq].add(course.code)

    # print(leadto_dict)


def populate_database():
    cursor = conn.cursor()  # db connection
    for course in course_list:
        try:
            cursor.execute(
                """INSERT INTO courses (courseid, description, prereqs, coreqs, equivalence, leadto)
                    VALUES (%s, %s, %s, %s, %s, %s);""",
                (course.code, course.desc,
                 convert_prereq(course.prq),
                 convert_coreq(course.corq),
                 desc_to_list(course.equ),
                 list(leadto_dict[course.code]))
            )
        except ValueError as ve:
            print('For the following course:')
            print(course.code)
            print('The following error occurred:')
            print(ve)
        except psycopg2.Error as e:
            print('For the following course:')
            print(course.code)
            print('The following error occurred:')
            print(e)
        else:
            print("indexed course: " + course.code)
    cursor.close()
    conn.commit()


def delete_table_contents():
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM courses;")
    except psycopg2.Error as e:
        print('The following error occurred:')
        print(e)
    else:
        cursor.close()
        conn.commit()
        print("successfully cleared all courses")


def convert_prereq(prereq_desc):
    # TODO transforms human readable into a predicate string
    return None


def convert_coreq(coreq_desc):
    # TODO transform human readable into predicate string
    return None


#  helper method returns a raw list course version from a description (prereq, coreq, equiv...)
def desc_to_list(desc):
    code_regex = re.compile("[A-Z]{4}\s[0-9]{3}")
    if desc is not None:
        desc_list = code_regex.findall(desc)
        # need to remove whitespaces in each value of the list
        for i, value in enumerate(desc_list):
            desc_list[i] = value.replace(" ", "")
        # print(desc_list)
        return desc_list
    else:
        return None

if __name__ == "__main__":
    main()
