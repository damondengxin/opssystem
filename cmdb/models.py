from django.db import models

# Create your models here.
class Assets(models.Model):
    assets_type_choices = (
        ('server', '服务器'),
        ('switch', '交换机'),
        ('route', '路由器'),
        ('printer', '打印机'),
        ('scanner', '扫描仪'),
        ('firewall', '防火墙'),
        ('storage', '存储设备'),
        ('wifi', '无线设备'),
    )
    assets_type = models.CharField(choices=assets_type_choices, max_length=100, default='server', verbose_name='资产类型')
    name = models.CharField(max_length=100, verbose_name='资产编号', unique=True)
    sn = models.CharField(max_length=100, verbose_name='设备序列号')
    buy_time = models.DateField(blank=True, null=True, verbose_name='购买时间')
    expire_date = models.DateField(u'过保修期', null=True, blank=True)
    buy_user = models.CharField(max_length=100, blank=True, null=True, verbose_name='购买人')
    management_ip = models.GenericIPAddressField(u'管理IP', blank=True, null=True)
    manufacturer = models.CharField(max_length=100, blank=True, null=True, verbose_name='制造商')
    provider = models.CharField(max_length=100, blank=True, null=True, verbose_name='供货商')
    model = models.CharField(max_length=100, blank=True, null=True, verbose_name='资产型号')
    status = models.SmallIntegerField(blank=True, null=True, verbose_name='状态')
    put_zone = models.SmallIntegerField(blank=True, null=True, verbose_name='放置区域')
    group = models.SmallIntegerField(blank=True, null=True, verbose_name='使用组')
    business = models.SmallIntegerField(blank=True, null=True, verbose_name='业务类型')
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'opssytem_assets'
        permissions = (
            ("can_read_assets", "读取资产权限"),
            ("can_change_assets", "更改资产权限"),
            ("can_add_assets", "添加资产权限"),
            ("can_delete_assets", "删除资产权限"),
        )
        verbose_name = '总资产表'
        verbose_name_plural = '总资产表'


class Server_Assets(models.Model):
    assets = models.OneToOneField('Assets')
    ip = models.CharField(max_length=100, unique=True, blank=True, null=True)
    hostname = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    passwd = models.CharField(max_length=100, blank=True, null=True)
    keyfile = models.SmallIntegerField(blank=True,
                                       null=True)  # FileField(upload_to = './upload/key/',blank=True,null=True,verbose_name='密钥文件')
    port = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    line = models.CharField(max_length=100, blank=True, null=True)
    cpu = models.CharField(max_length=100, blank=True, null=True)
    cpu_number = models.SmallIntegerField(blank=True, null=True)
    vcpu_number = models.SmallIntegerField(blank=True, null=True)
    cpu_core = models.SmallIntegerField(blank=True, null=True)
    disk_total = models.CharField(max_length=100, blank=True, null=True)
    ram_total = models.CharField(max_length=100, blank=True, null=True)
    kernel = models.CharField(max_length=100, blank=True, null=True)
    selinux = models.CharField(max_length=100, blank=True, null=True)
    swap = models.CharField(max_length=100, blank=True, null=True)
    raid = models.SmallIntegerField(blank=True, null=True)
    system = models.CharField(max_length=100, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)
    '''自定义添加只读权限-系统自带了add change delete三种权限'''

    class Meta:
        db_table = 'opssytem_server_assets'
        permissions = (
            ("can_read_server_assets", "读取服务器资产权限"),
            ("can_change_server_assets", "更改服务器资产权限"),
            ("can_add_server_assets", "添加服务器资产权限"),
            ("can_delete_server_assets", "删除服务器资产权限"),
        )
        verbose_name = '服务器资产表'
        verbose_name_plural = '服务器资产表'


class Network_Assets(models.Model):
    assets = models.OneToOneField('Assets')
    bandwidth = models.CharField(max_length=100, blank=True, null=True, verbose_name='背板带宽')
    ip = models.CharField(max_length=100, blank=True, null=True, verbose_name='管理ip')
    port_number = models.SmallIntegerField(blank=True, null=True, verbose_name='端口个数')
    firmware = models.CharField(max_length=100, blank=True, null=True, verbose_name='固件版本')
    cpu = models.CharField(max_length=100, blank=True, null=True, verbose_name='cpu型号')
    stone = models.CharField(max_length=100, blank=True, null=True, verbose_name='内存大小')
    configure_detail = models.TextField(max_length=100, blank=True, null=True, verbose_name='配置说明')
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'opssytem_network_assets'
        permissions = (
            ("can_read_network_assets", "读取网络资产权限"),
            ("can_change_network_assets", "更改网络资产权限"),
            ("can_add_network_assets", "添加网络资产权限"),
            ("can_delete_network_assets", "删除网络资产权限"),
        )
        verbose_name = '网络资产表'
        verbose_name_plural = '网络资产表'


class Disk_Assets(models.Model):
    assets = models.ForeignKey('Assets')
    device_volume = models.CharField(max_length=100, blank=True, null=True, verbose_name='硬盘容量')
    device_status = models.CharField(max_length=100, blank=True, null=True, verbose_name='硬盘状态')
    device_model = models.CharField(max_length=100, blank=True, null=True, verbose_name='硬盘型号')
    device_brand = models.CharField(max_length=100, blank=True, null=True, verbose_name='硬盘生产商')
    device_serial = models.CharField(max_length=100, blank=True, null=True, verbose_name='硬盘序列号')
    device_slot = models.SmallIntegerField(blank=True, null=True, verbose_name='硬盘插槽')
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'opssytem_disk_assets'
        permissions = (
            ("can_read_disk_assets", "读取磁盘资产权限"),
            ("can_change_disk_assets", "更改磁盘资产权限"),
            ("can_add_disk_assets", "添加磁盘资产权限"),
            ("can_delete_disk_assets", "删除磁盘资产权限"),
        )
        unique_together = (("assets", "device_slot"))
        verbose_name = '磁盘资产表'
        verbose_name_plural = '磁盘资产表'


class Ram_Assets(models.Model):
    assets = models.ForeignKey('Assets')
    device_model = models.CharField(max_length=100, blank=True, null=True, verbose_name='内存型号')
    device_volume = models.CharField(max_length=100, blank=True, null=True, verbose_name='内存容量')
    device_brand = models.CharField(max_length=100, blank=True, null=True, verbose_name='内存生产商')
    device_slot = models.SmallIntegerField(blank=True, null=True, verbose_name='内存插槽')
    device_status = models.CharField(max_length=100, blank=True, null=True, verbose_name='内存状态')
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'opssytem_ram_assets'
        permissions = (
            ("can_read_ram_assets", "读取内存资产权限"),
            ("can_change_ram_assets", "更改内存资产权限"),
            ("can_add_ram_assets", "添加内存资产权限"),
            ("can_delete_ram_assets", "删除内存资产权限"),
        )
        unique_together = (("assets", "device_slot"))
        verbose_name = '内存资产表'
        verbose_name_plural = '内存资产表'


class NetworkCard_Assets(models.Model):
    assets = models.ForeignKey('Assets')
    macaddress = models.CharField(u'MAC', max_length=64, unique=True)
    ipaddress = models.GenericIPAddressField(u'IP', blank=True, null=True)
    device_model = models.CharField(max_length=100, blank=True, null=True, verbose_name='网卡型号')
    device_brand = models.CharField(max_length=100, blank=True, null=True, verbose_name='网卡生产商')
    device_status = models.CharField(max_length=100, blank=True, null=True, verbose_name='网卡状态')
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'opssytem_networkcard_assets'
        permissions = (
            ("can_read_networkcard_assets", "读取网卡资产权限"),
            ("can_change_networkcard_assets", "更改网卡资产权限"),
            ("can_add_networkcard_assets", "添加网卡资产权限"),
            ("can_delete_networkcard_assets", "删除网卡资产权限"),
        )
        verbose_name = '网卡资产表'
        verbose_name_plural = '网卡资产表'


class Service_Assets(models.Model):
    '''业务分组表'''
    service_name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'opssytem_service_assets'
        permissions = (
            ("can_read_service_assets", "读取业务资产权限"),
            ("can_change_service_assets", "更改业务资产权限"),
            ("can_add_service_assets", "添加业务资产权限"),
            ("can_delete_service_assets", "删除业务资产权限"),
        )
        verbose_name = '业务分组表'
        verbose_name_plural = '业务分组表'


class Zone_Assets(models.Model):
    zone_name = models.CharField(max_length=100, unique=True)
    '''自定义权限'''

    class Meta:
        db_table = 'opssytem_zone_assets'
        permissions = (
            ("can_read_zone_assets", "读取机房资产权限"),
            ("can_change_zone_assets", "更改机房资产权限"),
            ("can_add_zone_assets", "添加机房资产权限"),
            ("can_delete_zone_assets", "删除机房资产权限"),
        )
        verbose_name = '机房资产表'
        verbose_name_plural = '机房资产表'


class Line_Assets(models.Model):
    line_name = models.CharField(max_length=100, unique=True)
    '''自定义权限'''

    class Meta:
        db_table = 'opssytem_line_assets'
        permissions = (
            ("can_read_line_assets", "读取出口线路资产权限"),
            ("can_change_line_assetss", "更改出口线路资产权限"),
            ("can_add_line_assets", "添加出口线路资产权限"),
            ("can_delete_line_assets", "删除出口线路资产权限"),
        )
        verbose_name = '出口线路资产表'
        verbose_name_plural = '出口线路资产表'


class Raid_Assets(models.Model):
    raid_name = models.CharField(max_length=100, unique=True)
    '''自定义权限'''

    class Meta:
        db_table = 'opssytem_raid_assets'
        permissions = (
            ("can_read_raid_assets", "读取Raid资产权限"),
            ("can_change_raid_assets", "更改Raid资产权限"),
            ("can_add_raid_assets", "添加Raid资产权限"),
            ("can_delete_raid_assets", "删除Raid资产权限"),
        )
        verbose_name = 'Raid资产表'
        verbose_name_plural = 'Raid资产表'


class Log_Assets(models.Model):
    assets_id = models.IntegerField(verbose_name='资产类型id', blank=True, null=True, default=None)
    assets_user = models.CharField(max_length=50, verbose_name='操作用户', default=None)
    assets_content = models.CharField(max_length=100, verbose_name='名称', default=None)
    assets_type = models.CharField(max_length=50, default=None)
    create_time = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='执行时间')

    class Meta:
        db_table = 'opssytem_log_assets'
        verbose_name = '项目配置操作记录表'
        verbose_name_plural = '项目配置操作记录表'