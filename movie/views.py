from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie

# Create your views here.

def home(request):
    #return HttpResponse('<h1>Welcome to home Page<h1>')
    #return render(request, 'home.html')
    #return render(request, 'home.html', {'name':'Juan Manuel López'})
    searchTerm = request.GET.get('searchMovie')
    movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm':searchTerm, 'movies': movies})

def about(request):
    return HttpResponse('<h1>Welcome to About Page </h1>')