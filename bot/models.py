from django.db import models


class Task(models.Model):
    key = models.CharField(max_length=200)
    summary = models.TextField()
    created_at = models.TimeField()

    def __str__(self):
        return self.summary

