from django.db import models
from django.urls import reverse
import os
from accounts.models import User
from datetime import date, datetime


class DailyReport(models.Model):
    day = models.DateField(initial=date.today())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body1 = models.TextField(null=True)
    body2 = models.TextField(null=True)
    body3 = models.TextField(null=True)
    body4 = models.TextField(null=True)
    body5 = models.TextField(null=True)
    body6 = models.TextField(null=True)
    # created_at = models.DateTimeField(auto_now_add=False)#impot-exportで任意にするため
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.day.strftime("%Y/%m/%d")

    class Meta:
        verbose_name_plural = "研修日報"


class ReadStates(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report = models.ForeignKey(DailyReport, on_delete=models.CASCADE, related_name='report_read')
    checked = models.BooleanField()
    # created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = "既読"