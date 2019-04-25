from django.db import models
from django.contrib.auth.models import AbstractUser

# models简表规定:
# 1 表明一律小写
# 2 每个表必须加上 META-db_table
# 3 字段名一律小写
# 4 related_name必须是由 db_table + 字段名构成
# 5 表明/字段 不能有下划线
# 6 数据创建时间 cretaetime
# 7 数据更新时间 updatetime


class userprofile(AbstractUser):

    role = models.IntegerField(
        verbose_name="角色",
        choices=(
            (0,"游客"),
            (1,"博主"),
            (2,"管理员"),
        ),
        default=0,
    )
    name = models.CharField(
        verbose_name="昵称",
        max_length=128,
        null=True,
        blank=True,
    )
    ip = models.CharField(
        verbose_name="最后登录ip",
        max_length=32,
        null=True,
        blank=True,
    )
    city = models.CharField(
        verbose_name="ip所在城市",
        max_length=128,
        null=True,
        blank=True,
    )
    images = models.TextField(
        verbose_name="用户头像",
        null=True,
        blank=True,
    )

    class Meta:
        db_table = 'user_userprofile'











