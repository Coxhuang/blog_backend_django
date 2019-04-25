from blog import models
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from blog.utils.mixins.mixin import MyListModeMixinBlog
from blog.article.list.list_blogarticle_serializer import ListBlogArticleblogSerializer



"""
1. blog 查看博文
"""
class ListBlogArticleblogView(MyListModeMixinBlog):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.blogarticle.objects.filter(is_secret=0).order_by("-createtime")
    serializer_class = ListBlogArticleblogSerializer
    msg_list = "查看博文列表"


