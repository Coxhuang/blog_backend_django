from django_restframework.mixins.mixin import MyCreateModeMixin
from user import models
from user.bloguser.operation.create.create_user_serializer import CreateBlogUseruserSerializer
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication





"""
1. user 新增博主
"""
class CreateBlogUseruserView(MyCreateModeMixin):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)
    queryset = models.userprofile.objects.all()
    serializer_class = CreateBlogUseruserSerializer
    msg_create = "注册成功"
    results_display = False # 是否显示序列化信息, 默认显示, 注册博主不能显示,因为有密码
