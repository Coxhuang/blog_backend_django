from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from blog import models


"""
1. blog 查看博文详细信息
"""
class DetailBlogArticleblogSerializer(DynamicFieldsMixin,serializers.ModelSerializer):

    is_secret = serializers.CharField(
        label="是否可见",
        source="get_is_secret_display",
    )
    createtime = serializers.SerializerMethodField(
        label="创建时间"
    )
    class Meta:
        model = models.blogarticle
        fields = [
            "id",
            "times",
            "detailimage",
            "title",
            "content",
            "createtime",
            "is_secret",
        ]

    def get_createtime(self,obj):

        return obj.createtime.strftime("%Y-%m-%d %H:%M:%S")



