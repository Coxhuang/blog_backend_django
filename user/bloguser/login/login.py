from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django_restframework.utils.auth.auth import checkauth
from django_restframework.utils.tokens.token import createtoken
from blog_backend.utils.captcha.check_captcha import captcha_instance

"""
1. 博主登录
"""
class userloginAPI(APIView):

    # authentication_classes = (JSONWebTokenAuthentication,)

    def post(self,request):

        user = checkauth.check_auth_user(
            username=request.data.get("username",None),
            password=request.data.get("password",None),
        ) # 校验用户名(邮箱)和密码
        token = createtoken.create_token(
            user=user
        ) # 生成token
        captcha_instance.check_captcha(
            timestamp=request.data.get("timestamp",None),
            captcha=request.data.get("captcha",None),
        )

        return Response({
            "success": True,
            "msg": "登录成功",
            "data": {
                "token": token
            }
        },status=status.HTTP_200_OK)


