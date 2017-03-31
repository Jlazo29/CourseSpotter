from django.db import models


class Course(models.Model):
    courseID = models.CharField(max_length=7)
    description = models.CharField(max_length=500)
    prereqs = models.CharField(max_length=200)
    coreqs = models.CharField(max_length=200)
    equivalence = []
    leadto = []
