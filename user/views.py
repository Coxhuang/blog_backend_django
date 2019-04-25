from django.shortcuts import HttpResponse
from user import models
from django_restframework.utils.tokens.token import createtoken
from rest_framework.views import APIView


class login_all_user(APIView):


    def post(self,request):

        username = request.data["username"]
        user = models.userprofile.objects.get(username=username)
        token = createtoken.create_token(user=user)

        return HttpResponse("TOKEN {}".format(token))







