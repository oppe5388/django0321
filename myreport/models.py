from django.db import models
from django.urls import reverse
import os
from accounts.models import User


class DailyReport(models.Model):
    day = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body1 = models.TextField(blank=True, null=True)
    body2 = models.TextField(blank=True, null=True)
    body3 = models.TextField(blank=True, null=True)
    body4 = models.TextField(blank=True, null=True)
    body5 = models.TextField(blank=True, null=True)
    body6 = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.day.strftime("%Y/%m/%d")

    class Meta:
        verbose_name_plural = "研修日報"


class CheckStates(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report = models.ForeignKey(DailyReport, on_delete=models.CASCADE, related_name='report_check')
    checked = models.BooleanField()

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = "LDチェック"