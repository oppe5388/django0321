# Generated by Django 3.2.12 on 2022-09-14 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myinfo', '0014_cas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fax',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('html', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'FAX当番',
            },
        ),
    ]
