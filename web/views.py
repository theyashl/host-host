from django.shortcuts import render, get_object_or_404
from .models import Movie


# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'web/movie_list.html', {'movies': movies})


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'web/movie_detail.html', {'movie': movie})
