from rest_framework.generics import get_object_or_404
from ..models import News, NewsTag


class QueryMixin:
    def get_query(self, tag_name):
        tag = get_object_or_404(NewsTag, tag_name=tag_name)
        if len(self.request.query_params) > 1:
            _from = int(self.request.query_params['from'])
            _too = int(self.request.query_params['too'])
            return News.objects.filter(news_tag=tag)[_from:_too]
        return News.objects.filter(news_tag=tag)[:5]