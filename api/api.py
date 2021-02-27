from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import NewsTag
from .serializers import NewsTagSerializer


class NewsView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(data={'data': 222})


class TagsViewSet(ReadOnlyModelViewSet):
    serializer_class = NewsTagSerializer
    queryset = NewsTag.objects.all()