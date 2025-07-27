from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Artist, Album

# Create your views here.

def home(request):
    return render(request, 'store/home.html')

def artist_list(request):
    artists = Artist.objects.all().order_by('debut_year')
    return render(request, 'store/artists.html', {'artists': artists})

def album_list(request):
    albums = Album.objects.select_related('artist').all().order_by('release_date')
    return render(request, 'store/albums.html', {'albums': albums})


def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, 'store/artist_detail.html',{'artist':artist})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'store/album_detail.html', {'album':album})

