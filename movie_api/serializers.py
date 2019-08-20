from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.validators import UniqueTogetherValidator

from .models import Comment, Movie
from .utils import get_movie


class MovieSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255, source='Title')

    class Meta:
        model = Movie
        exclude = ('Title',)
        read_only_fields = ('id', 'Year', 'Rated', 'Released', 'Runtime', 
                            'Genre', 'Director', 'Writer', 'Actors', 'Plot',
                            'Language', 'Country', 'Awards', 'Poster',
                            'Ratings', 'Metascore', 'imdbRating', 'imdbVotes',
                            'imdbID', 'Type', 'totalSeasons','DVD', 'BoxOffice',
                            'Production', 'Website', 'Response')

    def create(self, validated_data):
        '''creates movie model based on provided title 
            and data fetched from omdb api'''
        title = validated_data['Title']
        full_data = get_movie(title)
        try:
            return Movie.objects.get(Title=full_data['Title'])
        except Movie.DoesNotExist:
            return Movie.objects.create(**full_data)
        except KeyError:
            message = {'Error' : 'Movie not found. Please provide a valid title'}
            raise serializers.ValidationError(message)


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
