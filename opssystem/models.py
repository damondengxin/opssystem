from django.db import  models
from appdeploy.models import  Log_Ansible_Model,Log_Ansible_Playbook

class Global_Config(models.Model):
    ansible_model = models.SmallIntegerField(verbose_name='是否开启ansible模块操作记录', blank=True, null=True)
    ansible_playbook = models.SmallIntegerField(verbose_name='是否开启ansible剧本操作记录', blank=True, null=True)
    cron = models.SmallIntegerField(verbose_name='是否开启计划任务操作记录', blank=True, null=True)
    project = models.SmallIntegerField(verbose_name='是否开启项目操作记录', blank=True, null=True)
    assets = models.SmallIntegerField(verbose_name='是否开启资产操作记录', blank=True, null=True)
    server = models.SmallIntegerField(verbose_name='是否开启服务器命令记录', blank=True, null=True)
    email = models.SmallIntegerField(verbose_name='是否开启邮件通知', blank=True, null=True)

    class Meta:
        db_table = 'opssystem_global_config'


class Email_Config(models.Model):
    site = models.CharField(max_length=100, verbose_name='部署站点')
    host = models.CharField(max_length=100, verbose_name='邮件发送服务器')
    port = models.SmallIntegerField(verbose_name='邮件发送服务器端口')
    user = models.CharField(max_length=100, verbose_name='发送用户账户')
    passwd = models.CharField(max_length=100, verbose_name='发送用户密码')
    subject = models.CharField(max_length=100, verbose_name='发送邮件主题标识', default='[OPS]')
    cc_user = models.TextField(verbose_name='抄送用户列表', blank=True, null=True)

    class Meta:
        db_table = 'opssystem_email_config'


class Server_Command_Record(models.Model):
    user = models.CharField(max_length=50, verbose_name='远程用户')
    server = models.CharField(max_length=50, verbose_name='服务器IP')
    client = models.CharField(max_length=50, verbose_name='客户机IP', blank=True, null=True)
    command = models.TextField(verbose_name='历史命令', blank=True, null=True)
    etime = models.CharField(max_length=50, verbose_name='命令执行时间', unique=True)

    class Meta:
        db_table = 'opssystem_server_command_record'
        permissions = (
            ("can_read_server_command_record", "读取服务器操作日志权限"),
            ("can_change_server_command_record", "更改服务器操作日志权限"),
            ("can_add_server_command_record", "添加服务器操作日志权限"),
            ("can_delete_server_command_record", "删除服务器操作日志权限"),
        )
        verbose_name = '服务器操作日志表'
        verbose_name_plural = '服务器操作日志表'


class Ansible_CallBack_Model_Result(models.Model):
    logId = models.ForeignKey(Log_Ansible_Model)
    content = models.TextField(verbose_name='输出内容', blank=True, null=True)


class Ansible_CallBack_PlayBook_Result(models.Model):
    logId = models.ForeignKey(Log_Ansible_Playbook)
    content = models.TextField(verbose_name='输出内容', blank=True, null=True)