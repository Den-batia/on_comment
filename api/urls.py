from django.urls import path
from rest_framework import routers

from .api import TagsViewSet, NewsViewset, NewsPeopleViewSet, NewsRealtViewSet

router = routers.DefaultRouter()

router.register('v1/news-tags', TagsViewSet, 'news-tags')
router.register('v1/news/people', NewsPeopleViewSet, 'news-people')
router.register('v1/news/realt', NewsRealtViewSet, 'news-realt')
router.register('v1/news', NewsViewset, 'news')
urlpatterns = router.urls

# urlpatterns += [
#     path('v1/news/<uuid:tag_name>/', NewDealView.as_view(), name='new-deal')
# ]