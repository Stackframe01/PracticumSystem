from datetime import date

from django.db import models


class KeySkill(models.Model):
    name = models.CharField(max_length=255, primary_key=True)


class Vacancy(models.Model):
    created = models.DateField(auto_now=True)
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=5000)
    key_skills = models.ForeignKey(KeySkill, on_delete=models.CASCADE)
