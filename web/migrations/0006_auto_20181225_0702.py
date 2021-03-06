# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-25 07:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20181225_0411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='result',
        ),
        migrations.AddField(
            model_name='test',
            name='allnum',
            field=models.CharField(default='', max_length=2000, verbose_name='完成总次数请求'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='alltime',
            field=models.CharField(default='', max_length=2000, verbose_name='总用时'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='cgl',
            field=models.CharField(default='', max_length=2000, verbose_name='成功率'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='concurrency',
            field=models.CharField(default='', max_length=2000, verbose_name='实际最高并发连接数'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='data',
            field=models.CharField(default='', max_length=2000, verbose_name='传输数据'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='failed',
            field=models.CharField(default='', max_length=2000, verbose_name='失败次数'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='rate',
            field=models.CharField(default='', max_length=2000, verbose_name='平均每秒完成的请求次数'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='response',
            field=models.CharField(default='', max_length=2000, verbose_name='响应时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='successful',
            field=models.CharField(default='', max_length=2000, verbose_name='成功次数'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='throughput',
            field=models.CharField(default='', max_length=2000, verbose_name='每秒传输的数据'),
            preserve_default=False,
        ),
    ]
