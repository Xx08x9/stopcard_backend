from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

# Список всех продуктов
class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Детали одного продукта
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    from django.http import JsonResponse
from .models import Product, CartItem
import json