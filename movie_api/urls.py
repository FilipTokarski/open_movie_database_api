from .views import MovieViewset, CommentViewset, TopViewset
from django.urls import path

urlpatterns = [
    path('movies', MovieViewset.as_view(), name='movies'),
    path('comments', CommentViewset.as_view(), name='comments'),
    path('top', TopViewset.as_view(), name='top'),
]