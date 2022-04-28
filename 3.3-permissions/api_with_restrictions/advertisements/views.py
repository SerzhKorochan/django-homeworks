from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from .models import Advertisement
from .serializers import AdvertisementSerializer
from .filters import AdvertisementFilter
from .permissions import IsAdminOrOwnerOrReadOnly


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter
    
    @action(detail = True, methods = ['PATCH'])    
    def add_favourite(self, request, pk=None):
        try:
            creator_id = self.queryset.get(id=pk).creator.id
        except ObjectDoesNotExist:
            msg = 'Invalid advertisement id.'
            return Response(data={'response': msg}, status = status.HTTP_400_BAD_REQUEST)

        if creator_id != request.user.id:
            request.user.favourites.add(pk)
            msg = 'Success'
            return Response(data = {'response': msg}, status=status.HTTP_200_OK)
        else:
            msg = 'You can not add your own adv to favourite list.'
            return Response(data = {'response': msg}, status = status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['GET'])
    def get_favourites(self, request):
        data = [AdvertisementSerializer(obj).data for obj in request.user.favourites.all()]
        return Response(data=data, status=status.HTTP_200_OK)

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsAdminOrOwnerOrReadOnly()]
        elif self.action in ["add_favourite", "get_favourites"]:
            return [IsAuthenticated()]
            
        return []
