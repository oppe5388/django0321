# Generated by Django 3.2.12 on 2022-10-09 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myinfo', '0015_fax'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='入会コース')),
            ],
        ),
        migrations.CreateModel(
            name='ClassDrop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='プルダウン車種クラス')),
            ],
        ),
        migrations.CreateModel(
            name='ParentCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='サービス商品')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myprofit.category', verbose_name='入会コース')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myprofit.parentcategory', verbose_name='サービス商品'),
        ),
        migrations.CreateModel(
            name='CarDrop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='車名')),
                ('base_digit', models.CharField(max_length=10, verbose_name='基本3桁')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myprofit.classdrop', verbose_name='紐付く車種プルダウン')),
            ],
        ),
    ]
