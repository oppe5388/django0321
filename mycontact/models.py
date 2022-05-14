from django.db import models
from django.urls import reverse
import os


# class Dealers(models.Model):
#     code5 = models.CharField(max_length=10, verbose_name="コード5桁")
#     code4 = models.CharField(max_length=10, verbose_name="コード4桁")
#     name = models.CharField(max_length=50, verbose_name="販社略")
#     full_name = models.CharField(max_length=50, verbose_name="販社フル")
#     domain = models.CharField(max_length=100, verbose_name="ドメイン")
#     customer_desk = models.CharField(max_length=50, verbose_name="お客様相談室")
#     emergency = models.CharField(max_length=50, verbose_name="緊急サポートダイヤル")
#     bc = models.CharField(max_length=50, verbose_name="BC本部")
#     nfs = models.CharField(max_length=50, verbose_name="NFSメンテ")
#     in_house = models.CharField(max_length=50, verbose_name="自社メンテ")
#     base = models.CharField(max_length=50, verbose_name="事務所")
#     base_tel = models.CharField(max_length=50, verbose_name="事務所TEL")

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name_plural = "販社"


# class Shops(models.Model):
#     dealer = models.ForeignKey(Dealers, null=True, on_delete=models.PROTECT)
#     name = models.CharField(max_length=50, null=True, verbose_name="店名")
#     shopcode = models.CharField(max_length=10, null=True, verbose_name="店舗コード")
#     tel = models.CharField(max_length=50, null=True, verbose_name="TEL")
#     fax = models.CharField(max_length=50, null=True, verbose_name="FAX")
#     homepage = models.CharField(max_length=200, null=True, verbose_name="H.P.")
#     memo = models.CharField(max_length=100, null=True, verbose_name="メモ")
#     kana = models.CharField(max_length=50, null=True, verbose_name="フリガナ")

#     def __str__(self):
#         return self.name
        
#     class Meta:
#         verbose_name_plural = "店舗"


# class Contacts(models.Model):
#     incoming = models.CharField(max_length=20, verbose_name="相手")
#     name = models.TextField(max_length=100, verbose_name="窓口")
#     title = models.TextField(max_length=100, verbose_name="業務")
#     job = models.TextField(max_length=1000, verbose_name="詳細")
#     tel = models.TextField(max_length=100, verbose_name="TEL")
#     hours = models.TextField(max_length=100, verbose_name="時間")
#     searchwords = models.CharField(max_length=200, null=True, blank=True, verbose_name="検索ワード")
#     attachments = models.ManyToManyField('myinfo.Attachments', blank=True)
#     dealers = models.ManyToManyField(Dealers, blank=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name_plural = "問い合わせ先"