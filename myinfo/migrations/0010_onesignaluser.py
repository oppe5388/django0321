# Generated by Django 3.2.12 on 2022-06-02 13:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myinfo', '0009_auto_20220529_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='OneSignalUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('onesignal_user_id', models.CharField(max_length=255, verbose_name='OneSignalUserID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
            ],
        ),
    ]
