from django.db import models
from django.urls import reverse
import os

class MoneyTrans(models.Model):

    transfer = models.DateField(verbose_name="送金日")
    deadline = models.DateField(verbose_name="到着締切")
    entry = models.DateField(verbose_name="登録日")
    fix = models.DateField(verbose_name="承認日")
    setoff = models.DateField(verbose_name="相殺締切")

    def __str__(self):
        return self.transfer.strftime("%Y/%m/%d")

    class Meta:
        verbose_name_plural = "送金スケジュール"