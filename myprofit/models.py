from django.db import models

# Create your models here.
class ParentCategory(models.Model):
    name = models.CharField('サービス商品', max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('入会コース', max_length=255)
    parent = models.ForeignKey(ParentCategory, verbose_name='サービス商品', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

# テスト用に不要だが用意
class Post(models.Model):
    title = models.CharField('タイトル', max_length=255)
    category = models.ForeignKey(Category, verbose_name='入会コース', on_delete=models.PROTECT)

    def __str__(self):
        return self.title