from api.serializers import ProductSerializer, OrderSerializer
from api.models import Product, Order, OrderItem

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404


@api_view(["GET"])
def product_list(request):
    products = Product.objects.all()
    serializers = ProductSerializer(products, many=True)
    return Response(serializers.data)


@api_view(["GET"])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializers = ProductSerializer(product)
    return Response(serializers.data)


@api_view(["GET"])
def order_list(request):
    orders = Order.objects.all()
    serializers = OrderSerializer(orders, many=True)
    return Response(serializers.data)
