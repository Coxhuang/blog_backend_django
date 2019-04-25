from blog import models
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from blog.utils.mixins.mixin import MyUpdateModelMixinBlog
from blog.article.update.update_blogarticle_serializer import UpdateBlogArticleblogSerializer



"""
1. blog 修改博文
"""
class UpdateBlogArticleblogView(MyUpdateModelMixinBlog):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.blogarticle.objects.all()
    serializer_class = UpdateBlogArticleblogSerializer
    msg_list = "修改成功"
    lookup_field = "id"


