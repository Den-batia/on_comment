from rest_framework.serializers import ModelSerializer

from .api import NewsTag, News


class NewsTagSerializer(ModelSerializer):
    class Meta:
        model = NewsTag
        fields = ('id', 'tag_name',)


class TagSerializer(ModelSerializer):
    class Meta:
        model = NewsTag
        fields = ('tag_name',)


class NewsSerializer(ModelSerializer):
    news_tag = TagSerializer()

    class Meta:
        model = News
        fields = ('news_img_link', 'news_text', 'news_tag', 'post_date')