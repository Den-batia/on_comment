from rest_framework.serializers import ModelSerializer

from .api import NewsTag, News


class NewsTagSerializer(ModelSerializer):
    class Meta:
        model = NewsTag
        fields = ('id', 'tag_name', 'news')


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = ('news_img_link', )