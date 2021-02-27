from rest_framework.serializers import ModelSerializer

from .api import NewsTag


class NewsTagSerializer(ModelSerializer):
    class Meta:
        model = NewsTag
        fields = ('id', 'tag_name')