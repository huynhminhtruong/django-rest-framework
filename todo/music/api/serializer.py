from rest_framework import serializers
from music.models import Song

class SongSerializer(serializers.Serializer):
    class Meta:
        model = Song
        fields = ("title", "created")