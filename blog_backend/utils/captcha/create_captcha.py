from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from blog_backend.utils.redis.redis3 import redis3
from blog_backend.utils.captcha.captcha import create_captcha
from blog_backend.utils.encrypt import encrypt
from django.conf import settings





class CreateCaptcha(APIView):

    def create_captcha(self):
        """生成验证码"""

        ret = create_captcha()
        key, timestamp = encrypt.hash_sha1_encrypt(ret["code"].upper()) # 大写

        redis3.set(timestamp, key, settings.CAPTCHA_EXPIRE)

        return ret["base64"],timestamp

    def post(self,request):

        src,timestamp = self.create_captcha()

        return Response({
            "success": True,
            "msg": "成功获取验证码",
            "data": {
                "src":src,
                "timestamp":timestamp
            }
        }, status=status.HTTP_200_OK)