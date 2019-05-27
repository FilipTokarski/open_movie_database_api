from django.db.models import Count
from django.db.models.expressions import F, Window
from django.db.models.functions.window import DenseRank
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .models import Comment, Movie
from .serializers import CommentSerializer, MovieSerializer, TopSerializer


class MovieViewset(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class CommentViewset(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        # without get parameters lists all Comment objects
        queryset = Comment.objects.all()

        # with get parameters filters Comment objects by movie id
        if self.request.query_params.get('movie_id'):
            id_filter = self.request.query_params.get('movie_id')
            queryset = queryset.filter(movie=id_filter)
            return queryset

        return queryset


class TopViewset(ModelViewSet):
    serializer_class = TopSerializer

    def get_queryset(self):
        # Override queryset to get filtered results and rank
        queryset = Movie.objects.all()
        dense_rank = Window(expression=DenseRank(),
                            order_by=F('total_comments').desc())

        # filter by date
        if self.request.query_params:
            date_start = self.request.query_params.get('date_start')
            date_end = self.request.query_params.get('date_end')
            filtered_query = queryset.filter(
                                    comments__date_added__gte = date_start,
                                    comments__date_added__lte = date_end)
                                    
            # create 'total_comments' and calculated 'rank' fields
            queryset = filtered_query\
                                .annotate(total_comments=Count('comments'))\
                                .order_by('-total_comments')\
                                .annotate(rank=dense_rank)
            return queryset

        queryset = queryset.annotate(total_comments=Count('comments'))\
                           .order_by('-total_comments')\
                           .annotate(rank=dense_rank)
        return queryset
