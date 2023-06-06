from django.db import models
from django.utils import timezone

#添付ファイル
from django.core.validators import FileExtensionValidator
from tinymce import models as tinymce_models

class Task(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    # request_content = models.TextField()
    request_content = tinymce_models.HTMLField(null=True, blank=True)
    is_completed = models.BooleanField(default=False, help_text='完了')
    release_date = models.DateField(null=True, blank=True)
    # response_content = models.TextField(blank=True)
    response_content = tinymce_models.HTMLField(null=True, blank=True)
    # notes = models.TextField(blank=True)
    notes = tinymce_models.HTMLField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "st課題管理"