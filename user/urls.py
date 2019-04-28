from django.urls import path,include
from rest_framework import routers
from user import views
from user.bloguser.operation.create.create_user_viewset import CreateBlogUseruserView

CreateBlogUseruserViewRouter = routers.DefaultRouter() # 新增博主
CreateBlogUseruserViewRouter.register('', CreateBlogUseruserView)


urlpatterns = [
    path('login_all_user/', views.login_all_user.as_view()),
    path('createbloguser/', include(CreateBlogUseruserViewRouter.urls)), # 新增博主
]
