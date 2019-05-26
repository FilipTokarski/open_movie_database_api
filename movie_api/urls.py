from .views import MovieViewset, CommentViewset, TopViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'movies', MovieViewset, basename='movies')
router.register(r'comments', CommentViewset, basename='comments')
router.register(r'top', TopViewset, basename='top')

urlpatterns = router.urls