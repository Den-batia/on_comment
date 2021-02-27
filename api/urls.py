from django.urls import path
from rest_framework import routers

from .api import NewsView, TagsViewSet

router = routers.DefaultRouter()

router.register('v1/news-tags', TagsViewSet, 'news-tags')

urlpatterns = router.urls

urlpatterns += [
    path('v1/news', NewsView.as_view(), name='news'),
]