# Generated by Django 3.2.12 on 2022-05-02 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycontact', '0004_shops'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shops',
            old_name='code5',
            new_name='dealer',
        ),
    ]
