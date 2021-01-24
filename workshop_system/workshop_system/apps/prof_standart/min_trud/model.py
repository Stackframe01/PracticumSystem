from django.db import models


class JobTitle(models.Model):
    name = models.CharField(max_length=500)


class ProfessionalStandart(models.Model):
    code = models.CharField(max_length=255, unique=True)
    created = models.DateField(auto_now=True)
    name = models.CharField(max_length=500)
    job_titles = models.ManyToManyField(JobTitle)
    found_by = models.CharField(max_length=500)
