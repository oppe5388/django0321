# Generated by Django 3.2.12 on 2023-08-09 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystell', '0003_HTMLtoTextarea'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/st/', verbose_name='画像'),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateField(blank=True, null=True, verbose_name='発生日'),
        ),
        migrations.AlterField(
            model_name='task',
            name='is_completed',
            field=models.BooleanField(default=False, verbose_name='完了'),
        ),
        migrations.AlterField(
            model_name='task',
            name='release_date',
            field=models.DateField(blank=True, null=True, verbose_name='リリース日'),
        ),
        migrations.AlterField(
            model_name='task',
            name='request_content',
            field=models.TextField(blank=True, null=True, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='task',
            name='response_content',
            field=models.TextField(blank=True, null=True, verbose_name='回答'),
        ),
    ]
