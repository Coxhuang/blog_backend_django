from blog import models
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from blog.utils.mixins.mixin import MyRetrieveModelMixinBlog
from blog.article.detail.detail_blogarticle_serializer import DetailBlogArticleblogSerializer
from django.db.models import F


"""
1. blog 查看博文详细信息
"""
class DetailBlogArticleblogView(MyRetrieveModelMixinBlog):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.blogarticle.objects.all()
    serializer_class = DetailBlogArticleblogSerializer
    msg_list = "查看博文详细信息"
    lookup_field = "id"

    def __add_visitor_num(self,*args,**kwargs):
        instance = self.get_object()
        instance.times = F("times") + 1
        instance.save()
        return None

    def initial(self, request, *args, **kwargs):
        super(DetailBlogArticleblogView, self).initial(request, *args, **kwargs)
        self.__add_visitor_num() # 访客自增


