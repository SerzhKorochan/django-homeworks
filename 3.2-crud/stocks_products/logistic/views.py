from rest_framework.viewsets import ModelViewSet
from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer
from rest_framework.filters import SearchFilter
import django_filters


class StockFilter(django_filters.rest_framework.FilterSet):
    products = django_filters.CharFilter(field_name='positions__product__title', lookup_expr='icontains')

    class Meta:
        model = Stock
        fields = ['products']


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = StockFilter
