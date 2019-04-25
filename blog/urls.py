from django.urls import path,include
from rest_framework import routers
from blog.article.create.create_blogarticle_viewset import CreateBlogArticleblogView
from blog.article.list.list_blogarticle_viewset import ListBlogArticleblogView
from blog.article.detail.detail_blogarticle_viewset import DetailBlogArticleblogView
from blog.article.update.update_blogarticle_viewset import UpdateBlogArticleblogView
from blog.article.delete.delete_blogarticle_viewset import DeleteBlogArticleblogView

CreateBlogArticleblogViewRouter = routers.DefaultRouter() # 新增博文
CreateBlogArticleblogViewRouter.register('', CreateBlogArticleblogView)
ListBlogArticleblogViewRouter = routers.DefaultRouter() # 查看博文列表
ListBlogArticleblogViewRouter.register('', ListBlogArticleblogView)
DetailBlogArticleblogViewRouter = routers.DefaultRouter() # 查看博文详细信息
DetailBlogArticleblogViewRouter.register('', DetailBlogArticleblogView)
UpdateBlogArticleblogViewRouter = routers.DefaultRouter() # 修改博文
UpdateBlogArticleblogViewRouter.register('', UpdateBlogArticleblogView)
DeleteBlogArticleblogViewRouter = routers.DefaultRouter() # 删除博文
DeleteBlogArticleblogViewRouter.register('', DeleteBlogArticleblogView)


urlpatterns = [
    path('createblogarticle/', include(CreateBlogArticleblogViewRouter.urls)),
    path('listblogarticle/', include(ListBlogArticleblogViewRouter.urls)),
    path('detailblogarticle/', include(DetailBlogArticleblogViewRouter.urls)),
    path('updateblogarticle/', include(UpdateBlogArticleblogViewRouter.urls)),
    path('deleteblogarticle/', include(DeleteBlogArticleblogViewRouter.urls)),
]
