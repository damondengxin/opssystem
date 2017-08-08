from django.db import models

# Create your models here.

class Log_Ansible_Model(models.Model):
    ans_user = models.CharField(max_length=50, verbose_name='使用用户', default=None)
    ans_model = models.CharField(max_length=100, verbose_name='模块名称', default=None)
    ans_args = models.CharField(max_length=500, blank=True, null=True, verbose_name='模块参数', default=None)
    ans_server = models.TextField(verbose_name='服务器', default=None)
    create_time = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='执行时间')

    class Meta:
        db_table = 'opssystem_log_ansible_model'
        permissions = (
            ("can_read_log_ansible_model", "读取Ansible模块执行记录权限"),
            ("can_change_log_ansible_model", "更改Ansible模块执行记录权限"),
            ("can_add_log_ansible_model", "添加Ansible模块执行记录权限"),
            ("can_delete_log_ansible_model", "删除Ansible模块执行记录权限"),
        )
        verbose_name = 'Ansible模块执行记录表'
        verbose_name_plural = 'Ansible模块执行记录表'


class Ansible_Playbook(models.Model):
    playbook_name = models.CharField(max_length=50, verbose_name='剧本名称', unique=True)
    playbook_desc = models.CharField(max_length=200, verbose_name='功能描述', blank=True, null=True)
    playbook_vars = models.TextField(verbose_name='模块参数', blank=True, null=True)
    playbook_uuid = models.CharField(max_length=50, verbose_name='唯一id')
    playbook_file = models.FileField(upload_to='./upload/playbook/', verbose_name='剧本路径')
    playbook_auth_group = models.SmallIntegerField(verbose_name='授权组', blank=True, null=True)
    playbook_auth_user = models.SmallIntegerField(verbose_name='授权用户', blank=True, null=True, )

    class Meta:
        db_table = 'opssystem_ansible_playbook'
        permissions = (
            ("can_read_ansible_playbook", "读取Ansible剧本权限"),
            ("can_change_ansible_playbook", "更改Ansible剧本权限"),
            ("can_add_ansible_playbook", "添加Ansible剧本权限"),
            ("can_delete_ansible_playbook", "删除Ansible剧本权限"),
        )
        verbose_name = 'Ansible剧本配置表'
        verbose_name_plural = 'Ansible剧本配置表'


class Log_Ansible_Playbook(models.Model):
    ans_id = models.IntegerField(verbose_name='id', blank=True, null=True, default=None)
    ans_user = models.CharField(max_length=50, verbose_name='使用用户', default=None)
    ans_name = models.CharField(max_length=100, verbose_name='模块名称', default=None)
    ans_content = models.CharField(max_length=100, default=None)
    ans_server = models.TextField(verbose_name='服务器', default=None)
    create_time = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='执行时间')

    class Meta:
        db_table = 'opssystem_log_ansible_playbook'
        verbose_name = 'Ansible剧本操作记录表'
        verbose_name_plural = 'Ansible剧本操作记录表'


class Ansible_Playbook_Number(models.Model):
    playbook = models.ForeignKey('Ansible_Playbook', related_name='server_number', on_delete=models.CASCADE)
    playbook_server = models.CharField(max_length=100, verbose_name='目标服务器', blank=True, null=True)

    class Meta:
        db_table = 'opssystem_ansible_playbook_number'
        permissions = (
            ("can_read_ansible_playbook_number", "读取Ansible剧本成员权限"),
            ("can_change_ansible_playbook_number", "更改Ansible剧本成员权限"),
            ("can_add_ansible_playbook_number", "添加Ansible剧本成员权限"),
            ("can_delete_ansible_playbook_number", "删除Ansible剧本成员权限"),
        )
        verbose_name = 'Ansible剧本成员表'
        verbose_name_plural = 'Ansible剧本成员表'

    def __str__(self):
        return '%s' % (self.playbook_server)