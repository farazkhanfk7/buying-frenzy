from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from django.db.models.query_utils import Q
from .models import Menu, Restaurant
from .serializers import MenuSerializer, UserSerializer, RestaurantSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated,permissions.IsAdminUser]


@permission_classes((permissions.AllowAny,)) # This decorator to be used with APIView
class RestaurantList(APIView):
    """
    List of all Available Hospitals
    """

    def get(self, request, format=None):
        range = self.request.query_params.get('show')
        if range is not None:
            price_gt = self.request.query_params.get('price_gt')
            price_lt = self.request.query_params.get('price_lt')
            instance = Restaurant.objects.filter(menu__price__gte=price_gt).distinct()
            instance = instance[:int(range)]
            serializer = RestaurantSerializer(instance, many=True, context={'request':request})
            return Response(serializer.data)
        else: 
            instance = Restaurant.objects.all()
            serializer = RestaurantSerializer(instance, many=True)
            return Response(serializer.data)
