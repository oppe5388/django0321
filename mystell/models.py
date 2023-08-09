from django.db import models
from django.utils import timezone

#添付ファイル
from django.core.validators import FileExtensionValidator
from tinymce import models as tinymce_models

class Task(models.Model):
    # created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateField(null=True, blank=True, verbose_name="発生日")
    
    request_content = models.TextField(null=True, blank=True, verbose_name="内容")
    # request_content = tinymce_models.HTMLField(null=True, blank=True)
    
    is_completed = models.BooleanField(default=False, verbose_name="完了") #help_text='完了'
    release_date = models.DateField(null=True, blank=True, verbose_name="リリース日")
    
    response_content = models.TextField(null=True, blank=True, verbose_name="回答")
    # response_content = tinymce_models.HTMLField(null=True, blank=True)
    
    notes = models.TextField(null=True, blank=True)
    # notes = tinymce_models.HTMLField(null=True, blank=True)
    
    # 画像を格納するためのフィールド
    image = models.ImageField(upload_to = 'uploads/st/', null=True, blank=True, verbose_name='画像')
    
    class Meta:
        verbose_name_plural = "st課題管理"