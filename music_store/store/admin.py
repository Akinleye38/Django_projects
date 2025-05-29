from django.contrib import admin
from .models import Artist, Album

# Register your models here.

class AlbumInLine(admin.TabularInline):
    model = Album
    extra = 1
    
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'debut_year')
    ordering = ('debut_year',)
    inlines = [AlbumInLine]
    
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'artist')
    list_filter = ('artist',)
    ordering = ('release_date',)    