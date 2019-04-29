from django_restframework.exceptions import exception
from django.contrib.auth import authenticate



class CheckAuth(object):


    def check_auth_user(self,*args,**kwargs):

        username = kwargs.get('username',None)
        password = kwargs.get('password',None)
        user = authenticate(
            username=username,
            password=password,
        )
        if not user:
            raise exception.myException400({
                "success": False,
                "msg": "账号密码不匹配",
            })

        return user

checkauth = CheckAuth()

