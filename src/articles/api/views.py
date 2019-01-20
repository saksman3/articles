from rest_framework.generics import ListAPIView, RetrieveAPIView,RetrieveUpdateAPIView
from rest_framework.viewsets import ModelViewSet
from articles.models import Article
from .serializers import ArticleSerializer

class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()