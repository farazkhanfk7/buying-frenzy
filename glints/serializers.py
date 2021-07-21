from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Purchase, Restaurant, Menu, OpeningTime

weekdays = {1:"Mon",2:"Tues",3:"Weds",4:"Thurs",5:"Fri",6:"Sat",7:"Sun"}

class UserSerializer(serializers.ModelSerializer):
    staff_of = serializers.StringRelatedField()
    class Meta:
        model = User
        fields = ['url', 'username', 'email','staff_of']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['dishName','price']

class OpeningTimeSerializer(serializers.Serializer):
    weekday = serializers.SerializerMethodField() 
    from_hour = serializers.TimeField(format="%H:%M")
    to_hour = serializers.TimeField(format="%H:%M")
    
    def get_weekday(self, instance):
        return weekdays[instance.weekday]
    
    class Meta:
        model = OpeningTime
        fields = ['weekday','from_hour','to_hour']

class RestaurantSerializer(serializers.ModelSerializer):
    menu = serializers.SerializerMethodField('get_menu')

    class Meta:
        model = Restaurant
        fields = ['restaurantName','cashBalance','menu','openingHours']

    def get_menu(self, instance):
        price_gt = self.context["request"].query_params.get('price_gt')
        price_lt = self.context["request"].query_params.get('price_lt')
        if price_gt: 
            filtered_menu = Menu.objects.filter(available_in=instance,price__gte=price_gt,price__lt=price_lt)
        else:
            filtered_menu = Menu.objects.filter(available_in=instance)
        serializer = MenuSerializer(filtered_menu, many=True)
        return serializer.data

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['openingHours'] = OpeningTimeSerializer(instance.openingHours, many=True).data
        return response

class PurchaseSerializer(serializers.ModelSerializer):
    transactionDate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S %p", required=False)

    class Meta:
        model = Purchase
        fields = ['purchase_id','purchaser','menu_bought','restaurant','dishName','restaurantName','transactionAmount','transactionDate','success']