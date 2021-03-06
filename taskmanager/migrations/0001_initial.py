# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 02:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cron_Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cron_minute', models.CharField(default=None, max_length=10, verbose_name='分')),
                ('cron_hour', models.CharField(default=None, max_length=10, verbose_name='时')),
                ('cron_day', models.CharField(default=None, max_length=10, verbose_name='天')),
                ('cron_week', models.CharField(default=None, max_length=10, verbose_name='周')),
                ('cron_month', models.CharField(default=None, max_length=10, verbose_name='月')),
                ('cron_user', models.CharField(default=None, max_length=50, verbose_name='任务用户')),
                ('cron_name', models.CharField(default=None, max_length=100, verbose_name='任务名称')),
                ('cron_desc', models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='任务描述')),
                ('cron_command', models.CharField(default=None, max_length=200, verbose_name='任务参数')),
                ('cron_script', models.FileField(blank=True, default=None, null=True, upload_to='./upload/cron/', verbose_name='脚本路径')),
                ('cron_script_path', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='脚本路径')),
                ('cron_status', models.SmallIntegerField(default=None, verbose_name='任务状态')),
                ('cron_server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.Server_Assets')),
            ],
            options={
                'verbose_name': '任务配置表',
                'db_table': 'opssystem_cron_config',
                'permissions': (('can_read_cron_config', '读取任务配置权限'), ('can_change_cron_config', '更改任务配置权限'), ('can_add_cron_config', '添加任务配置权限'), ('can_delete_cron_config', '删除任务配置权限')),
                'verbose_name_plural': '任务配置表',
            },
        ),
        migrations.CreateModel(
            name='Log_Cron_Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cron_id', models.IntegerField(blank=True, default=None, null=True, verbose_name='id')),
                ('cron_user', models.CharField(default=None, max_length=50, verbose_name='操作用户')),
                ('cron_name', models.CharField(default=None, max_length=100, verbose_name='名称')),
                ('cron_content', models.CharField(default=None, max_length=100)),
                ('cron_server', models.CharField(default=None, max_length=100)),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='执行时间')),
            ],
            options={
                'verbose_name': '任务配置操作记录表',
                'db_table': 'opssystem_log_cron_config',
                'verbose_name_plural': '任务配置操作记录表',
            },
        ),
        migrations.AlterUniqueTogether(
            name='cron_config',
            unique_together=set([('cron_name', 'cron_server', 'cron_user')]),
        ),
    ]
