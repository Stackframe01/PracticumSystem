from django.db import models


class KeySkill(models.Model):
    name = models.CharField(max_length=255)


class Vacancy(models.Model):
    code = models.CharField(max_length=255)
    created = models.DateField(auto_now=True)
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=5000, null=True)
    key_skills = models.ManyToManyField(KeySkill)
