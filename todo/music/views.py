from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Song
from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from .api.serializer import SongSerializer

# Create your views here.

class SongListView(ListView):
    model = Song
    template = "music/template/list_view.html"

class SongDetailsView(DetailView):
    model = Song
    template = "music/template/details_view.html"
