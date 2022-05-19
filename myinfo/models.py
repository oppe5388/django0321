from django.db import models
# from django.contrib.auth.models import User
from accounts.models import User
 
from django.urls import reverse
import os

#添付ファイル
from django.core.validators import FileExtensionValidator
from tinymce import models as tinymce_models


# class InfoCategory(models.Model):
#     name = models.CharField(max_length=100, null=True, verbose_name="カテゴリ名")
#     sort_no = models.IntegerField(verbose_name="ソートNo")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name_plural = "カテゴリ"


# Informationクラス
class Information(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # category = models.ForeignKey(InfoCategory, null=True, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    # body = models.TextField()
    body = tinymce_models.HTMLField(null=True, blank=True)
    to_flag = models.CharField(max_length=100, null=True, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=False)#impot-exportで任意にするため
    # updated_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=False)#更新するしないでソートをコントロールするため
    is_draft = models.BooleanField(default=False, blank=True, help_text='下書き')
    freeword = models.CharField(max_length=100, null=True, blank=True)
     
    def __str__(self):
        return self.title
        # return f"{self.category} {self.title}"

    class Meta:
        verbose_name_plural = "お知らせ"

    def get_absolute_url(self):
        return reverse('myinfo:detail', kwargs={'pk':self.pk})

class ReadStates(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    information = models.ForeignKey(Information, on_delete=models.CASCADE, related_name='info_read')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = "既読"


class Notifications(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    information = models.ForeignKey(Information, on_delete=models.CASCADE, related_name='info_notifi')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # return self.user
        return str(self.user)

    class Meta:
        verbose_name_plural = "通知"


class InfoComments(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    information = models.ForeignKey(Information, on_delete=models.CASCADE)
    #commentはSQL競合のためバッククオートでくくる？
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment[:20]#開始20文字

    class Meta:
        verbose_name_plural = "コメント"


class Attachments(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    file_path = models.FileField(
        upload_to = 'uploads/%Y/%m/%d/',
        # verbose_name = 'attached file',
        # validators=[FileExtensionValidator(['jpg', ])],
        null = True
    )
    
    information = models.ForeignKey(
        Information, verbose_name='紐づくお知らせ',
        blank=True, null=True,
        on_delete=models.CASCADE,
        related_name='info_attach',
    )

    # def __str__(self):
    #     return self.name

    """ -----file_name属性として作成----- """
    def file_name(self):
        path = os.path.basename(self.file_path.name)  # ファイル名のみ抽出
        return path

    def __str__(self):
        path = os.path.basename(self.file_path.name)  # ファイル名のみ抽出
        return path

    class Meta:
        verbose_name_plural = "添付ファイル"


class WorkShifts(models.Model):
    file_path = models.FileField(upload_to = 'uploads/')
    created_at = models.DateTimeField(auto_now_add=False)

    """ -----file_name属性として作成----- """
    def file_name(self):
        path = os.path.basename(self.file_path.name)  # ファイル名のみ抽出
        return path

    class Meta:
        verbose_name_plural = "シフト"


class Dealers(models.Model):
    code5 = models.CharField(max_length=10, verbose_name="コード5桁")
    code4 = models.CharField(max_length=10, verbose_name="コード4桁")
    name = models.CharField(max_length=50, verbose_name="販社略")
    full_name = models.CharField(max_length=50, verbose_name="販社フル")
    domain = models.CharField(max_length=100, verbose_name="ドメイン")
    customer_desk = models.CharField(max_length=50, verbose_name="お客様相談室")
    emergency = models.CharField(max_length=50, verbose_name="緊急サポートダイヤル")
    bc = models.CharField(max_length=50, verbose_name="BC本部")
    nfs = models.CharField(max_length=50, verbose_name="NFSメンテ")
    in_house = models.CharField(max_length=50, verbose_name="自社メンテ")
    base = models.CharField(max_length=50, verbose_name="事務所")
    base_tel = models.CharField(max_length=50, verbose_name="事務所TEL")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "販社"


class Shops(models.Model):
    dealer = models.ForeignKey(Dealers, null=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name="店名")
    shopcode = models.CharField(max_length=10, null=True, blank=True, verbose_name="店舗コード")
    tel = models.CharField(max_length=50, null=True, blank=True, verbose_name="TEL")
    fax = models.CharField(max_length=50, null=True, blank=True, verbose_name="FAX")
    homepage = models.CharField(max_length=200, null=True, blank=True, verbose_name="H.P.")
    memo = models.CharField(max_length=100, null=True, blank=True, verbose_name="メモ")
    kana = models.CharField(max_length=50, null=True, blank=True, verbose_name="フリガナ")

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = "店舗"


class Contacts(models.Model):
    incoming = models.CharField(max_length=20, verbose_name="相手")
    name = models.TextField(max_length=100, verbose_name="窓口")
    title = models.TextField(max_length=100, verbose_name="業務")
    job = models.TextField(max_length=1000, verbose_name="詳細")
    tel = models.TextField(max_length=100, verbose_name="TEL")
    hours = models.TextField(max_length=100, verbose_name="時間")
    searchwords = models.CharField(max_length=200, null=True, blank=True, verbose_name="検索ワード")
    attachments = models.ManyToManyField(Attachments, blank=True)
    # attachments = models.ManyToManyField(Attachments, blank=True, through="ContactAttachRel",)
    dealers = models.ManyToManyField(Dealers, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "問い合わせ先"


# FAQクラス
class Faqs(models.Model):
    question = tinymce_models.HTMLField(null=True, blank=True)
    answer1 = tinymce_models.HTMLField(null=True, blank=True)
    answer2 = tinymce_models.HTMLField(null=True, blank=True)
    reference = tinymce_models.HTMLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=False)#impot-exportで任意にするため
    updated_at = models.DateTimeField(auto_now_add=False)#更新するしないでソートをコントロールするため
    contacts = models.ManyToManyField(Contacts, blank=True)
    attachments = models.ManyToManyField(Attachments, blank=True)
    dealers = models.ManyToManyField(Dealers, blank=True)
     
    def __str__(self):
        return str(self.question)

    class Meta:
        verbose_name_plural = "FAQ"


# class ContactAttachRel(models.Model):
#     contact = models.ForeignKey("Contacts", on_delete=models.CASCADE)
#     attachment = models.ForeignKey("Attachments", on_delete=models.CASCADE)