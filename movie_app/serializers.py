from typing import Type

from rest_framework import serializers

from movie_app.models import Director, Movie, Review


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model= Review
        fields = '__all__'
