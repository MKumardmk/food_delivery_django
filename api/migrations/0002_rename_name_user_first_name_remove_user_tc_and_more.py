# Generated by Django 4.0.4 on 2023-01-19 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='tc',
        ),
        migrations.AddField(
            model_name='user',
            name='device_token',
            field=models.CharField(default='eQJM6WkmQZ6wTKJGLU74hw:APA91bHkQp4-dw3zSqf9Pn53u4ed7o_XWH0eFou7-ZITVAYaZU2K97kPmt9KUlRtsnDYjqImBaMGVBq67J91jMCpy1jpDKVZYIJc1rVN6jODqNYPwZ0bc-J8DdXjp3LckGsi_BXMHXya', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='device_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
