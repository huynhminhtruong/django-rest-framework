from django.urls import path, include
from rest_framework import routers
from . import views

app_name = "music"

urlpatterns = [
    path('', views.SongListView.as_view(), name="list"),
    path('<int:pk>/', views.SongDetailsView.as_view(), name="details")
]