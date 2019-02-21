# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-01-03 01:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_issue_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='src_path',
            field=models.CharField(blank=True, max_length=2048, null=True, verbose_name='上传文件路径'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='path',
            field=models.CharField(blank=True, max_length=2048, null=True, verbose_name='备份文件路径'),
        ),
    ]