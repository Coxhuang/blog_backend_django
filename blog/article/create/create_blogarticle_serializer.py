from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from blog import models
from django_restframework.serializers.serializer import error_instance


"""
1. blog 新增博文
"""
class CreateBlogArticleblogSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    title = serializers.CharField(
        label="标题",
        required=True,
        min_length=1,
        max_length=130,
        error_messages=error_instance.field_errormsg(field="标题")
    )
    content = serializers.CharField(
        label="内容",
        required=True,
        error_messages=error_instance.field_errormsg(field="内容")
    )
    is_secret = serializers.CharField(
        label="是否可见",
        required=True,
        error_messages=error_instance.field_errormsg(field="是否可见")
    )
    class Meta:
        model = models.blogarticle
        fields = [
            "title",
            "content",
            "is_secret",
        ]

    def create(self, validated_data):

        user = self.context["request"].user

        user = models.blogarticle.objects.create(
            user = user,
            **validated_data
        )

        return user

