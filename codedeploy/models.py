from django.db import models

# Create your models here.

class Project_Config(models.Model):
    project_repertory_choices = (
        ('git', 'git'),
        ('svn', 'svn'),
    )
    deploy_model_choices = (
        ('branch', 'branch'),
        ('tag', 'tag'),
    )
    project_env = models.CharField(max_length=50, verbose_name='项目环境', default=None)
    project_name = models.CharField(max_length=100, verbose_name='项目名称', default=None)
    project_local_command = models.TextField(blank=True, null=True, verbose_name='部署服务器要执行的命令', default=None)
    project_repo_dir = models.CharField(max_length=100, verbose_name='本地仓库目录', default=None)
    project_dir = models.CharField(max_length=100, verbose_name='代码目录', default=None)
    project_exclude = models.TextField(blank=True, null=True, verbose_name='排除文件', default=None)
    project_address = models.CharField(max_length=100, verbose_name='版本仓库地址', default=None)
    project_uuid = models.CharField(max_length=50, verbose_name='唯一id')
    project_repo_user = models.CharField(max_length=50, verbose_name='仓库用户名', blank=True, null=True)
    project_repo_passwd = models.CharField(max_length=50, verbose_name='仓库密码', blank=True, null=True)
    project_repertory = models.CharField(choices=project_repertory_choices, max_length=10, verbose_name='仓库类型',
                                         default=None)
    project_status = models.SmallIntegerField(verbose_name='是否激活', blank=True, null=True, default=None)
    project_remote_command = models.TextField(blank=True, null=True, verbose_name='部署之后执行的命令', default=None)
    project_user = models.CharField(max_length=50, verbose_name='项目文件宿主', default=None)
    project_model = models.CharField(choices=deploy_model_choices, max_length=10, verbose_name='上线类型', default=None)
    project_audit_group = models.SmallIntegerField(verbose_name='项目授权组', blank=True, null=True, default=None)
    '''自定义权限'''

    class Meta:
        db_table = 'opssystem_project_config'
        permissions = (
            ("can_read_project_config", "读取项目权限"),
            ("can_change_project_config", "更改项目权限"),
            ("can_add_project_config", "添加项目权限"),
            ("can_delete_project_config", "删除项目权限"),
        )
        unique_together = (("project_env", "project_name"))
        verbose_name = '项目管理表'
        verbose_name_plural = '项目管理表'


class Log_Project_Config(models.Model):
    project_id = models.IntegerField(verbose_name='资产类型id', blank=True, null=True, default=None)
    project_user = models.CharField(max_length=50, verbose_name='操作用户', default=None)
    project_name = models.CharField(max_length=100, verbose_name='名称', default=None)
    project_content = models.CharField(max_length=100, default=None)
    project_branch = models.CharField(max_length=100, default=None, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='执行时间')

    class Meta:
        db_table = 'opssystem_log_project_config'
        verbose_name = '项目配置操作记录表'
        verbose_name_plural = '项目配置操作记录表'


class Project_Number(models.Model):
    project = models.ForeignKey('Project_Config', related_name='project_number', on_delete=models.CASCADE)
    server = models.CharField(max_length=100, verbose_name='服务器IP', default=None)
    dir = models.CharField(max_length=100, verbose_name='项目目录', default=None)

    class Meta:
        db_table = 'opssystem_project_number'
        permissions = (
            ("can_read_project_number", "读取项目成员权限"),
            ("can_change_project_number", "更改项目成员权限"),
            ("can_add_project_number", "添加项目成员权限"),
            ("can_delete_project_number", "删除项目成员权限"),
        )
        unique_together = (("project", "server"))
        verbose_name = '项目成员表'
        verbose_name_plural = '项目成员表'

    def __str__(self):
        return '%s' % (self.server)


class Project_Order(models.Model):
    STATUS = (
        (0, '已通过'),
        (1, '已拒绝'),
        (2, '审核中'),
        (3, '已部署'),
    )
    LEVEL = (
        (0, '非紧急'),
        (1, '紧急'),
    )
    order_user = models.CharField(max_length=30, verbose_name='工单申请人')
    order_project = models.ForeignKey('Project_Config', verbose_name='项目id')
    order_subject = models.CharField(max_length=200, verbose_name='工单申请主题')
    order_content = models.TextField(verbose_name='工单申请内容')
    order_branch = models.CharField(max_length=50, blank=True, null=True, verbose_name='分支版本')
    order_comid = models.CharField(max_length=100, blank=True, null=True, verbose_name='版本id')
    order_tag = models.CharField(max_length=50, blank=True, null=True, verbose_name='标签')
    order_audit = models.CharField(max_length=30, verbose_name='部署指派人')
    order_status = models.IntegerField(choices=STATUS, default='审核中', verbose_name='工单状态')
    order_level = models.IntegerField(choices=LEVEL, default='非紧急', verbose_name='工单紧急程度')
    order_cancel = models.TextField(blank=True, null=True, verbose_name='取消原因')
    create_time = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='工单发布时间')
    modify_time = models.DateTimeField(auto_now=True, blank=True, verbose_name='工单最后修改时间')
    '''自定义权限'''

    class Meta:
        db_table = 'opssystem_project_order'
        permissions = (
            ("can_read_project_order", "读取项目部署权限"),
            ("can_change_project_order", "更改项目部署权限"),
            ("can_add_project_order", "添加项目部署权限"),
            ("can_delete_project_order", "删除项目部署权限"),
        )
        unique_together = (("order_project", "order_subject", "order_user"))
        verbose_name = '项目部署工单表'
        verbose_name_plural = '项目部署工单表'

