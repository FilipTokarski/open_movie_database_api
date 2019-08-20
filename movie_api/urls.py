from .views import MovieViewset, CommentViewset, TopViewset
from django.urls import path
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'movies', MovieViewset, basename='movies')
# router.register(r'comments', CommentViewset, basename='comments')
# router.register(r'top', TopViewset, basename='top')

# urlpatterns = router.urls

urlpatterns = [
    path('movies', MovieViewset.as_view(), name='movies'),
    path('comments', CommentViewset.as_view(), name='comments'),
    path('top', TopViewset.as_view(), name='top'),
]