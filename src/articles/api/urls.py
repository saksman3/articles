from articles.api.views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ArticleViewSet)
urlpatterns = router.urls


""" from .views import ArticleDetailView, ArticleListView

urlpatterns=[
    path('',ArticleListView.as_view()),
    path('<pk>',ArticleDetailView.as_view())
] """