from blog.article.create.create_blogarticle_serializer import CreateBlogArticleblogSerializer
from blog import models
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from blog.utils.mixins.mixin import MyCreateModeMixinBlog



"""
1. blog 新增博文
"""
class CreateBlogArticleblogView(MyCreateModeMixinBlog):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.blogarticle.objects.all()
    serializer_class = CreateBlogArticleblogSerializer
    msg_create = "新增成功"
    # results_display = False # 是否显示序列化信息, 默认显示, 注册博主不能显示, 因为有密码
