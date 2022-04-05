from django.db import models
from django.urls import reverse
import os

class Contacts(models.Model):

    incoming = models.CharField(max_length=20, verbose_name="相手")
    name = models.TextField(max_length=100, verbose_name="窓口")
    title = models.TextField(max_length=100, verbose_name="業務")
    job = models.TextField(max_length=1000, verbose_name="詳細")
    tel = models.TextField(max_length=100, verbose_name="TEL")
    hours = models.TextField(max_length=100, verbose_name="時間")
    searchwords = models.CharField(max_length=200, null=True, blank=True, verbose_name="検索ワード")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "問い合わせ先"