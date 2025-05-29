from django.shortcuts import render

# Create your views here.
from .models import Artist, Album

def home(request):
    return render(request, 'store/home.html')

def artist_list(request):
    artists = Artist.objects.all().order_by('debut_year')
    return render(request, 'store/artists.html', {'artists': artists})

def album_list(request):
    albums = Album.objects.select_related('artist').all().order_by('release_date')
    return render(request, 'store/albums.html', {'albums': albums})

