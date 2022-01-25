from django.shortcuts import render
from rest_framework import viewsets
from users.models import CustomUser
from users.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    """
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = CustomUser.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        return Response(request.method)

    def retrieve(self, request, pk=None):
        # queryset = CustomUser.objects.all()
        # user = get_object_or_404(queryset, pk=pk)
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset)
        return Response(serializer.data)

    def update(self, request, pk=None):
        return Response(request.method)

    def partial_update(self, request, pk=None):
        return Response('request.method')

    def destroy(self, request, pk=None):
        return Response(request.method)
    """
