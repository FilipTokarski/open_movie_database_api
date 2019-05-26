from rest_framework import serializers
from rest_framework.response import Response

from .models import Comment, Movie
from .utils import get_movie


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('id', 'Year', 'Rated', 'Released', 'Runtime', 
                            'Genre', 'Director', 'Writer', 'Actors', 'Plot',
                            'Language', 'Country', 'Awards', 'Poster',
                            'Ratings', 'Metascore', 'imdbRating', 'imdbVotes',
                            'imdbID', 'Type', 'totalSeasons','DVD', 'BoxOffice',
                            'Production', 'Website', 'Response')

    def create(self, validated_data):
        title = validated_data['Title']
        full_data = get_movie(title)
        movie = Movie.objects.create(**full_data)
        return movie


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('movie', 'content', 'date_added')
        read_only_fields = ('date_added',)


class TopSerializer(serializers.ModelSerializer):

    movie_id = serializers.IntegerField(source='id', read_only=True)
    total_comments = serializers.IntegerField(read_only=True)
    rank = serializers.IntegerField(read_only=True)

    class Meta:
        model = Movie
        fields = ('movie_id', 'total_comments', 'rank')
