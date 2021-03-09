from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import NewsTag, News
from .serializers import NewsTagSerializer, NewsSerializer
from .Mixins.QueryMixin import QueryMixin


class TagsViewSet(ReadOnlyModelViewSet):
    serializer_class = NewsTagSerializer
    queryset = NewsTag.objects.all()


class NewsViewset(ReadOnlyModelViewSet, QueryMixin):
    serializer_class = NewsSerializer

    def get_queryset(self):
        return self.get_query()


class NewsPeopleViewSet(ReadOnlyModelViewSet, QueryMixin):
    serializer_class = NewsSerializer

    def get_queryset(self):
        return self.get_query(tag_name='people')


class NewsRealtViewSet(ReadOnlyModelViewSet, QueryMixin):
    serializer_class = NewsSerializer

    def get_queryset(self):
        return self.get_query(tag_name='realt')


class NewsTechViewSet(ReadOnlyModelViewSet, QueryMixin):
    serializer_class = NewsSerializer

    def get_queryset(self):
        return self.get_query(tag_name='tech')


class NewsAutoViewSet(ReadOnlyModelViewSet, QueryMixin):
    serializer_class = NewsSerializer

    def get_queryset(self):
        return self.get_query(tag_name='auto')