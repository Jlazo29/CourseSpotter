from django.shortcuts import render
from django.http import HttpResponse
import psycopg2

conn = psycopg2.connect(
    dbname="dbj5dke7k2llc2",
    user="tkybpgvuevmgyp",
    password="fce7442d8e5a39771caae45610673a14ff60325a71ed5170748e2f5bd7c95d79",
    host="ec2-23-21-220-167.compute-1.amazonaws.com",
    port="5432"
)


def index(request):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses;")
    data = cursor.fetchone()
    print(data)

    return HttpResponse("Hello, world")


def course_detail(request, course_id):
    return HttpResponse("Page for course: %s." % course_id)
