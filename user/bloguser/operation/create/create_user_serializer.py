from django_restframework.serializers.serializer import error_instance
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from user import models
from django_restframework.serializers.serializer import MySerializer






"""
1. user 新增博主
"""
class CreateBlogUseruserSerializer(MySerializer):

    username = serializers.CharField(
        label="用户名",
        validators=[UniqueValidator(queryset=models.userprofile.objects.all())],
        required=True,
        min_length=3,
        max_length=16,
        error_messages=error_instance.field_errormsg(field="用户名")
    )
    password = serializers.CharField(
        label="密码",
        required=True,
        min_length=6,
        max_length=16,
        error_messages=error_instance.field_errormsg(field="密码")
    )

    class Meta:
        model = models.userprofile
        fields = [
            "username",
            "password",
        ]
        extra_kwargs = {
            'username': {'required': True},
            'password': {'required': True},
        }

    def create(self, validated_data):
        user = models.userprofile.objects.create_user(
            role = 1,
            **validated_data
        )

        return user


