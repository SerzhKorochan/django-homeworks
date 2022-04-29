from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
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

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(~Q(status='DRAFT'))

        if request.user.is_authenticated:
            drafts = self.get_queryset().filter(
                status = 'DRAFT',
                creator = request.user.id
            )
            queryset = queryset | drafts

        queryset = self.filter_queryset(queryset)
        serializer = self.get_serializer(queryset, many=True)

        return Response(data = serializer.data)

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsAdminOrOwnerOrReadOnly()]
        elif self.action in ["add_favourite", "get_favourites"]:
            return [IsAuthenticated()]
            
        return []
