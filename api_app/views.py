from django.db.models.query import QuerySet
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404, response
from .serializers import CartItemSerializer
from .models import CartItem


# https://stackabuse.com/creating-a-rest-api-with-django-rest-framework/

class CartItemViews(APIView):

    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        data = CartItem.objects.all()
        serializer = CartItemSerializer(data, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


class CartItemDetailViews(APIView):

    def get_object(self, id):
        try:
            return CartItem.objects.get(id=id)
        except CartItem.DoesNotExist:
            raise Http404

    def get(self, request, id):
        item = self.get_object(id)
        serializer = CartItemSerializer(item)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, id):
        item = self.get_object(id)
        serializer = CartItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        item = self.get_object(id)
        serializer = CartItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        item = self.get_object(id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"}, status=status.HTTP_204_NO_CONTENT)


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['product_name']
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['product_name']
    search_fields = ['product_name']

# Filtering and object lookups DjangoFilterBackend
# http://example.com/api/products?category=clothing&in_stock=True

# SearchFilter
# http://example.com/api/users?search=russell
# search_fields = ['username', 'email', 'profile__profession']
# '^' Starts-with search.
# '=' Exact matches.
# '@' Full-text search. (Currently only supported Django's PostgreSQL backend.)
# '$' Regex search.
# search_fields = ['=username', '=email']

# OrderingFilter
# http://example.com/api/users?ordering=username
# http://example.com/api/users?ordering=account,username

# Specifying which fields may be ordered against
# filter_backends = [filters.OrderingFilter]
# ordering_fields = ['username', 'email']

# Specifying a default ordering
# ordering = ['username']
