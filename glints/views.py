from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from django.db.models.query_utils import Q
from .models import Menu, Restaurant
from rest_framework import filters
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
        show = self.request.query_params.get('show')
        day = self.request.query_params.get('day')
        time = self.request.query_params.get('time')
        if show is not None:
            price_gt = self.request.query_params.get('price_gt')
            price_lt = self.request.query_params.get('price_lt')
            instance = Restaurant.objects.filter(menu__price__gte=price_gt).distinct()
            instance = instance[:int(show)]
        elif day and time:
            weekday = str(day)
            time = str(time)
            instance = Restaurant.objects.filter(openingHours__weekday=weekday,
                                                 openingHours__from_hour__lte=time,
                                                 openingHours__to_hour__gte=time)
        else: 
            instance = Restaurant.objects.all()
        serializer = RestaurantSerializer(instance, many=True, context={'request':request})
        return Response(serializer.data)


class RestaurantSearchView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['restaurantName']

