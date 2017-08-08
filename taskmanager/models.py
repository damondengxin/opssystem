from django.db import models
from cmdb.models import  Server_Assets

# Create your models here.
class Cron_Config(models.Model):
    cron_server = models.ForeignKey(Server_Assets)
    cron_minute = models.CharField(max_length=10, verbose_name='分', default=None)
    cron_hour = models.CharField(max_length=10, verbose_name='时', default=None)
    cron_day = models.CharField(max_length=10, verbose_name='天', default=None)
    cron_week = models.CharField(max_length=10, verbose_name='周', default=None)
    cron_month = models.CharField(max_length=10, verbose_name='月', default=None)
    cron_user = models.CharField(max_length=50, verbose_name='任务用户', default=None)
    cron_name = models.CharField(max_length=100, verbose_name='任务名称', default=None)
    cron_desc = models.CharField(max_length=200, blank=True, null=True, verbose_name='任务描述', default=None)
    cron_command = models.CharField(max_length=200, verbose_name='任务参数', default=None)
    cron_script = models.FileField(upload_to='./upload/cron/', blank=True, null=True, verbose_name='脚本路径', default=None)
    cron_script_path = models.CharField(max_length=100, blank=True, null=True, verbose_name='脚本路径', default=None)
    cron_status = models.SmallIntegerField(verbose_name='任务状态', default=None)

    class Meta:
        db_table = 'opssystem_cron_config'
        permissions = (
            ("can_read_cron_config", "读取任务配置权限"),
            ("can_change_cron_config", "更改任务配置权限"),
            ("can_add_cron_config", "添加任务配置权限"),
            ("can_delete_cron_config", "删除任务配置权限"),
        )
        verbose_name = '任务配置表'
        verbose_name_plural = '任务配置表'
        unique_together = (("cron_name", "cron_server", "cron_user"))


class Log_Cron_Config(models.Model):
    cron_id = models.IntegerField(verbose_name='id', blank=True, null=True, default=None)
    cron_user = models.CharField(max_length=50, verbose_name='操作用户', default=None)
    cron_name = models.CharField(max_length=100, verbose_name='名称', default=None)
    cron_content = models.CharField(max_length=100, default=None)
    cron_server = models.CharField(max_length=100, default=None)
    create_time = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='执行时间')

    class Meta:
        db_table = 'opssystem_log_cron_config'
        verbose_name = '任务配置操作记录表'
        verbose_name_plural = '任务配置操作记录表'