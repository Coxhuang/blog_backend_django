from blog import models
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from blog.utils.mixins.mixin import MyDeleteModelMixinBlog
from blog.article.delete.delete_blogarticle_serializer import DeleteBlogArticleblogSerializer



"""
1. blog 删除博文
"""
class DeleteBlogArticleblogView(MyDeleteModelMixinBlog):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.blogarticle.objects.all()
    serializer_class = DeleteBlogArticleblogSerializer
    msg_list = "删除博文"
    lookup_field = "id"


