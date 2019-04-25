from django_restframework.exceptions import exception


class BlogModeMixinPlug(object):

    def check_user(self,*args,**kwargs):

        request = kwargs["request"]
        user = request.user
        if user.role != 1:
            raise exception.myException403({
                "success": False,
                "msg": "非博主账号"
            })

        return None

