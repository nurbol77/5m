from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    duration = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name="movies")



    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    stars = models.IntegerField(default=1, choices=[(i, i * '*') for i in range(6)])
    def __str__(self):
        return self.text
