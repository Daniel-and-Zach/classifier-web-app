from django.db import models

class CodeSnippet(models.Model):
    code = models.CharField(max_length=1000)
    answer = models.CharField(max_length=200)
