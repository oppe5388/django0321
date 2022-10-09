from django.db import models

class ParentCategory(models.Model):
    name = models.CharField('サービス商品', max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('入会コース', max_length=255)
    parent = models.ForeignKey(ParentCategory, verbose_name='サービス商品', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

# ↑テスト用に用意（データが入ることはない）
class Post(models.Model):
    title = models.CharField('タイトル', max_length=255)
    category = models.ForeignKey(Category, verbose_name='入会コース', on_delete=models.PROTECT)

    def __str__(self):
        return self.title


# プルダウン用の車種クラス
class ClassDrop(models.Model):
    name = models.CharField('プルダウン車種クラス', max_length=30)

    def __str__(self):
        return self.name
    
# プルダウンに紐付いた車名
class CarDrop(models.Model):
    name = models.CharField('車名', max_length=50)
    base_digit = models.CharField('基本3桁', max_length=10)
    parent = models.ForeignKey(ClassDrop, verbose_name='紐付く車種プルダウン', on_delete=models.PROTECT)

    def __str__(self):
        return self.name