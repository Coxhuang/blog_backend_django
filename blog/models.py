from django.db import models
from user.models import userprofile






class blogarticle(models.Model):

    user = models.ForeignKey(
        verbose_name="博主",
        to=userprofile,
        on_delete=models.DO_NOTHING,
        related_name="blog_blogarticle_user",
        null=False,
        blank=False,
    )
    title = models.CharField(
        verbose_name="博客标题",
        max_length=255,
        null=False,
        blank=False,
    )
    content = models.TextField(
        verbose_name="博文",
        null=False,
        blank=False,
    )
    createtime = models.DateTimeField(
        verbose_name="发表时间",
        auto_now_add=True, # 不会随着数据的改变,时间发生变化,只认定第一次的时间
    )
    updatetime = models.DateTimeField(
        verbose_name="最后更新时间",
        auto_now=True, # 只要有更新,时间就会更新
    )
    is_secret = models.IntegerField(
        verbose_name="对游客会否可见",
        choices=(
            (0,"可见"),
            (1,"私密"),
        ),
        default=1, # 默认可见
    )
    times = models.BigIntegerField(
        verbose_name="博文浏览量",
        default=0,
    )
    listimage = models.TextField(
        verbose_name="列表图片",
        null=True,
        blank=True,
    )
    detailimage = models.TextField(
        verbose_name="详细图片图片",
        null=True,
        blank=True,
    )

    class Meta:
        db_table = 'blog_blogarticle'


# class blogcomment(models.Model):
#     """博客评论"""
#
#     user = models.ForeignKey(
#         verbose_name="游客",
#         to=userprofile,
#         on_delete=models.DO_NOTHING,
#     )
#     blog = models.ForeignKey(
#         verbose_name="博文",
#         to=blogarticle,
#         on_delete=models.DO_NOTHING,
#     )
#     level = models.IntegerField(
#         verbose_name="楼层",
#         default=1,
#     )
#     comment = models.TextField(
#         verbose_name="评论",
#     )
#     # reply = models.ForeignKey(
#     #     verbose_name="对哪个游客回复",
#     #     to="self",
#     #     to_field="user",
#     #     related_name="blog_blogcomment_reply",
#     #     on_delete=models.DO_NOTHING,
#     #     null=True,
#     #     blank=True,
#     # )
#     cretaetime = models.DateTimeField(
#         verbose_name="回复时间",
#         auto_now_add=True
#     )
#     city = models.CharField(
#         verbose_name="ip所在城市",
#         max_length=128,
#         null=True,
#         blank=True,
#     )
#
#     class Meta:
#         # unique_together = ('user', 'remomeygroup',)
#         db_table = 'blog_blogcomment'


class blogtag(models.Model):
    """博客标签"""

    user = models.ForeignKey(
        verbose_name="博主",
        to=userprofile,
        on_delete=models.DO_NOTHING,
        related_name="blog_blogtag_user",
        null=False,
        blank=False,
    )
    blog = models.ManyToManyField(
        verbose_name="博客",
        to=blogarticle,
    )
    tag = models.CharField(
        verbose_name="标签",
        max_length=128,
    )

    class Meta:
        db_table = 'blog_blogtag'




