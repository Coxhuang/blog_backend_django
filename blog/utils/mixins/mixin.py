from rest_framework.views import APIView
from django_restframework.mixins.mixin import (
    MyCreateModeMixin,MyListModeMixin,MyDeleteModelMixin,
    MyRetrieveModelMixin,MyUpdateModelMixin
)
from blog.utils.mixins.mixinplug import BlogModeMixinPlug




"""
1. post create data
"""
class MyCreateModeMixinBlog(MyCreateModeMixin,BlogModeMixinPlug):

    def initial(self, request, *args, **kwargs):
        super(MyCreateModeMixinBlog, self).initial(request, *args, **kwargs)
        self.check_user(request=request) # 校验登录用户是否是博主


"""
2. delete destroy data
"""
class MyDeleteModelMixinBlog(MyDeleteModelMixin,BlogModeMixinPlug):

    def initial(self, request, *args, **kwargs):
        super(MyDeleteModelMixinBlog, self).initial(request, *args, **kwargs)
        self.check_user(request=request) # 校验登录用户是否是博主


"""
3. put update data
"""
class MyUpdateModelMixinBlog(MyUpdateModelMixin,BlogModeMixinPlug):
    def initial(self, request, *args, **kwargs):
        super(MyUpdateModelMixinBlog, self).initial(request, *args, **kwargs)
        self.check_user(request=request) # 校验登录用户是否是博主

"""
4. get list data
"""
class MyListModeMixinBlog(MyListModeMixin,BlogModeMixinPlug):
    def initial(self, request, *args, **kwargs):
        super(MyListModeMixinBlog, self).initial(request, *args, **kwargs)
        self.check_user(request=request) # 校验登录用户是否是博主

"""
5. get retrieve data
"""
class MyRetrieveModelMixinBlog(MyRetrieveModelMixin,BlogModeMixinPlug):
    def initial(self, request, *args, **kwargs):
        super(MyRetrieveModelMixinBlog, self).initial(request, *args, **kwargs)
        self.check_user(request=request) # 校验登录用户是否是博主

"""
6. APIView
"""
class MyAPIView(APIView,BlogModeMixinPlug):
    authentication_classes = ()
    permission_classes = ()

