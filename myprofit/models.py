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
    
    
#価格用車種クラス一覧を作る
# メーカー
class Maker(models.Model):
    name = models.CharField('メーカー', max_length=30)

    def __str__(self):
        return self.name
    
# 乗用ボディタイプ
class PassengerType(models.Model):
    name = models.CharField('乗用ボティタイプ', max_length=30)

    def __str__(self):
        return self.name
    
# 乗用サイズ
class PassengerSize(models.Model):
    name = models.CharField('乗用サイズ', max_length=30)

    def __str__(self):
        return self.name

# 商用ボディタイプ
class CargoType(models.Model):
    name = models.CharField('商用ボティタイプ', max_length=30)

    def __str__(self):
        return self.name
    
# 商用サイズ
class CargoSize(models.Model):
    name = models.CharField('商用サイズ', max_length=30)

    def __str__(self):
        return self.name
    
# 車名（価格用）
class CarForPrice(models.Model):
    name = models.CharField('車名', max_length=30)
    base_digit = models.CharField('基本3桁', max_length=200, null=True, blank=True)
    code = models.CharField('コード', max_length=10, null=True, blank=True)
    remarks = models.TextField('説明', null=True, blank=True)
    maker = models.ForeignKey(Maker, verbose_name='メーカー', on_delete=models.PROTECT)
    passenger_type = models.ForeignKey(PassengerType, verbose_name='乗用ボティタイプ', null=True, blank=True, on_delete=models.PROTECT)
    passenger_size = models.ForeignKey(PassengerSize, verbose_name='乗用サイズ', null=True, blank=True, on_delete=models.PROTECT)
    cargo_type = models.ForeignKey(CargoType, verbose_name='商用ボティタイプ', null=True, blank=True, on_delete=models.PROTECT)
    cargo_size = models.ForeignKey(CargoSize, verbose_name='商用サイズ', null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    