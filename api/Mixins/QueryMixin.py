from rest_framework.generics import get_object_or_404
from ..models import News, NewsTag


class QueryMixin:

    def get_query(self, tag_name=None):

        if len(self.request.query_params) > 1:
            _from = int(self.request.query_params['from'])
            _too = int(self.request.query_params['too'])
            if tag_name:
                tag = get_object_or_404(NewsTag, tag_name=tag_name)
                return News.objects.filter(news_tag=tag).order_by('-post_date')[_from:_too]
            return News.objects.all().order_by('-post_date')[_from:_too]

        if tag_name:
            tag = get_object_or_404(NewsTag, tag_name=tag_name)
            return News.objects.filter(news_tag=tag).order_by('-post_date')[:5]

        return News.objects.all().order_by('-post_date')[:5]