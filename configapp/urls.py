from django.urls import path

from configapp import views

urlpatterns = [
    path('movie/',views.index,name='movie' ),
    path('actor/',views.actor,name='actor' ),
]