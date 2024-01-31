from typing import Type

from rest_framework import serializers

from movie_app.models import Director, Movie, Review


def validate_name_min_length(value, min_length):
    if len(value) < min_length:
        raise serializers.ValidationError(f'Мин для этого поля  {min_length}')


class DirectorSerializers(serializers.ModelSerializer):
    movie_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = '__all__'

    def get_movie_count(self, obj):
        return obj.movies.conut()

    def validate_name(self, value):
        validate_name_min_length(value, 5)
        return value


class MovieSerializers(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'

    def get_average_rating(self, obj):
        total_stars = sum(review.stars for review in obj.reviews.all())
        num_reviews = obj.reviews.count()
        if num_reviews > 0:
            return total_stars / num_reviews
        return 0.0

    def validate_name(self, value):
        validate_name_min_length(value, 5)
        return value


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

        def validate_name(self, value):
            validate_name_min_length(value, 10)
            return value
