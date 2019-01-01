from music.api.viewset import SongViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("music", SongViewSet, base_name="music")