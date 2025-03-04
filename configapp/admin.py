from django.contrib import admin
from .models import *


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'genre')
    list_filter = ('year', 'genre')
    search_fields = ('name', 'year', 'genre')
    ordering = ('year',)


class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthdate')
    list_filter = ('name', 'birthdate')
    search_fields = ('name', 'birthdate')
    ordering = ('birthdate',)


admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor, ActorAdmin)