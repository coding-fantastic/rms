from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User 
from rest_framework.authtoken.views import Token


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = [ 'building' , 'floor', 'room', 'name', 'contact_info', 'payment']

        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = [ 'building' , 'floor', 'room', 'comment']


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ['building_name', 'city']

class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor 
        fields = ['building', 'floor_number']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room 
        fields = ['building', 'floor', 'room_number', 'room_status']
    
class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental 
        fields = ['building', 'floor', 'room', 'rental_amount' ]
    

