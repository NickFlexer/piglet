from django.db import models


class Task(models.Model):
    key = models.CharField(max_length=200)
    summary = models.TextField()
    created_at = models.TimeField()

    def __str__(self):
        return self.summary


class Setting(models.Model):
    topic = models.CharField(max_length=200)
    setting = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

    def __str__(self):
        return self.topic + "-" + self.setting
