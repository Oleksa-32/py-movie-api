from django.urls import path
from cinema.views import movie_list, movie_details

urlpatterns = [
    path("cinema/movies/", movie_list, name="cinema_list"),
    path("cinema/<int:pk>", movie_details, name="cinema_detail"),
]
app_name = "cinema"