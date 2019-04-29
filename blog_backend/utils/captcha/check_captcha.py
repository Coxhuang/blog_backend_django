from blog_backend.utils.redis.redis3 import redis3
from django_restframework.exceptions import exception
from blog_backend.utils.encrypt import encrypt




class Captcha(object):

    def check_captcha(self,*args,**kwargs):

        timestamp = kwargs.get("timestamp",None)
        captcha = kwargs.get("captcha",None)


        if (not timestamp) or (not redis3.get(timestamp)):
            raise exception.myException415({
                "success": False,
                "msg": "验证码失效,重新获取验证码",
            })

        code = encrypt.hash_sha1_decrypt(timestamp, captcha.upper())

        if code != redis3.get(timestamp):
            print("code:", code)
            print("redis3.get(times):", redis3.get(timestamp))
            raise exception.myException415({
                "success": False,
                "msg": "验证码错误",
            })

        redis3.delete(timestamp) # 删除缓存



        return None


captcha_instance = Captcha()