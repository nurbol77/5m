from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from movie_app.models import Director, Movie, Review
from movie_app.serializers import DirectorSerializers, MovieSerializers, ReviewSerializers


@api_view(['GET'])
def director_list(request):
    if request.method == 'GET':
        queryset = Director.objects.all()
        serializer = DirectorSerializers(queryset, many=True)
        return Response(serializer.data, status=200)


@api_view(['GET'])
def director_detail(request, id):
    if Movie.method == 'GET':
        queryset = get_object_or_404(Movie, id=id)
        serializer = MovieSerializers(queryset)
        return Response(serializer.data, status=200)


@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        queryset = Movie.objects.all()
        serializer = MovieSerializers(queryset, many=True)
        return Response(serializer.data, status=200)


@api_view(['GET'])
def movie_detail(request, id):
    if request.method == 'GET':
        queryset = get_object_or_404(Movie, id=id)
        serializer = MovieSerializers(queryset)
        return Response(serializer.data, status=200)


@api_view(['GET'])
def review_list(request):
    if request.method == 'GET':
        queryset = Review.objects.all()
        serializer = ReviewSerializers(queryset, many=True)
        return Response(serializer.data, status=200)


@api_view(['GET'])
def review_detail(request, id):
    if Movie.method == 'GET':
        queryset = get_object_or_404(Review, id=id)
        serializer = ReviewSerializers(queryset)
        return Response(serializer.data, status=200)
