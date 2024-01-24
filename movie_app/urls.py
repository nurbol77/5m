from django.urls import path

from movie_app import views

urlpatterns = [
    path('director/', views.director_list),
    path('director/<int:id>', views.director_detail),
    path('movie/', views.movie_list),
    path('movie/<int:id>', views.movie_detail),
    path('review/', views.review_list),
    path('review/<int:id>', views.review_detail),

]
