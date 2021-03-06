from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import NewsTag, News
from .serializers import NewsTagSerializer, NewsSerializer


class NewsView(APIView):
    def get(self, request, *args, **kwargs):
        news = News.objects.filter(post_date='1614960254').all()

        return Response(data={news[0].news_text, news[0].top_comment})


class TagsViewSet(ReadOnlyModelViewSet):
    serializer_class = NewsTagSerializer
    queryset = NewsTag.objects.all()


class NewsViewset(ReadOnlyModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()[:1]