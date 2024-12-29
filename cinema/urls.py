from django.urls import path
from cinema.views import cinema_list, cinema_details

urlpatterns = [
    path("cinema/movies/", cinema_list, name="cinema_list"),
    path("cinema/<int:pk>", cinema_details, name="cinema_detail"),
]
app_name = "cinema"