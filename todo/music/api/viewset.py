from music.models import Song
from .serializer import SongSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


# class SongViewSet(viewsets.ViewSet):
#
#     # list, create, retrieve, update, partial_update, destroy
#
#     def list(self, request):
#         queryset = Song.objects.all()
#         serializer = SongSerializer(queryset, many=True)
#         return Response(serializer.data)


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('created').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)