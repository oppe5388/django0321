# Generated by Django 3.2.12 on 2022-11-08 06:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myinfo', '0016_faxexplain_faxformats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holiday',
            name='title',
            field=models.CharField(choices=[('1', '発送なし'), ('2', 'VCC休み'), ('3', '非表示にする日'), ('4', '未着リスト用2次休業日')], max_length=100, verbose_name='分類'),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '小部屋',
            },
        ),
    ]
