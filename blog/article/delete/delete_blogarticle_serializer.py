from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from blog import models


"""
1. blog 删除博文
"""
class DeleteBlogArticleblogSerializer(DynamicFieldsMixin,serializers.ModelSerializer):

    class Meta:
        model = models.blogarticle
        fields = []



