from uuid import uuid4

from django.core.validators import MinValueValidator
from django.db import models


class NewsTag(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid4, editable=False)
    tag_name = models.TextField(max_length=20, default='')


class News(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid4, editable=False)
    news_tag = models.ForeignKey(NewsTag, on_delete=models.CASCADE, related_name='news')
    post_date = models.IntegerField(default=0)
    news_img_link = models.URLField(default='')
    news_link = models.URLField(default='')
    news_text = models.TextField(max_length=300)
    top_comment = models.TextField(max_length=300)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.news_text



