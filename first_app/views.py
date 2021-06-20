from django.db.models import manager
from rest_framework.serializers import Serializer
from first_app import products, serializers
from .serializers import ProductSerializers
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, response

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Products, Order, OrderItem, Review
# from .products import products
# from .models import Products
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/products/',
        '/api/products/create/',

        '/api/products/upload/',

        '/api/products/<id>/reviews/',
        
        '/api/products/top/',
        '/api/products/<id>/',

        '/api/products/delete/<id>/',
        '/api/products/<update>/<id>/',
    ]
    return Response(routes)

@api_view(['GET'])
def getProducts(request):
    queryset = Products.objects.all()
    serializer = ProductSerializers(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk):
    queryset = Products.objects.get(id=pk)
    serializer = ProductSerializers(queryset, many=False)  
    return Response(serializer.data)
















######
# @api_view(['GET'])
# def api_urls(request):
#     api_urls = {
#         'List': '/product-list/',
#         'Detail View': '/product-detail/<str:pk>',
#         'Create': '/product-create',
#         'Update': '/product-update/<str:pk>',
#         'Delete': '/product-delete/<str:pk>',

#     }
    
#     return Response(api_urls)


# @api_view(['GET'])
# def ProductList(request):
#     products = Products.objects.all()
#     serializer = ProductSerializers(products, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def ProductDetail(request, pk):
#     products = Products.objects.get(id=pk)
#     serializer = ProductSerializers(products, many=False)
#     return Response(serializer.data)

# @api_view(['POST'])
# def ProductCreate(request):
#     serializer = ProductSerializers(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['POST'])
# def ProductUpdate(request, pk):
#     product = Products.objects.get(id=pk)
#     serializer = ProductSerializers(instance=product, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)


# @api_view(['DELETE'])
# def ProductDelete(request, pk):
#     product = Products.objects.get(id=pk)
#     product.delete()

#     return Response('Item was deleted Successfully')