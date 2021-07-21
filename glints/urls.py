from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, RestaurantList, RestaurantSearchView, PaymentView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('restaurants/',RestaurantList.as_view(),name='restaurant-list'),
    path('restaurants/search/',RestaurantSearchView.as_view(),name='restaurant-filter'),
    path('purchase/', PaymentView.as_view(), name='purchase')
]
