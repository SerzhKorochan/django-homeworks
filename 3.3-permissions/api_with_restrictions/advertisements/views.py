from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Advertisement
from .serializers import AdvertisementSerializer
from .filters import AdvertisementFilter
from .permissions import IsOwnerOrReadOnly


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
            
        return []
