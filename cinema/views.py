from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from cinema.models import Movie
from cinema.serializers import MovieSerializer


@api_view(["GET", "POST"])
def cinema_list(request):
    if request.method == "GET":
        cinemas = Movie.objects.all()
        serializer = MovieSerializer(cinemas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET", "PUT", "DELETE"])
def cinema_details(request, pk):
    cinema = get_object_or_404(Movie, pk=pk)
    if request.method == "GET":
        serializer = MovieSerializer(cinema)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = MovieSerializer(cinema, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        cinema.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

