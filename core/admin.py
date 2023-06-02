from django.contrib import admin

from core.models import *
# Register your models here.

@admin.register(Building)

class BuildingModel(admin.ModelAdmin):
    list_filter =('buildingName', 'city' , 'createdAt', 'modifiedAt')
    list_display = ('buildingName' , 'city', 'createdAt', 'modifiedAt')
    

@admin.register(Room)

class RoomModel(admin.ModelAdmin):
    list_filter =('building','floor', 'roomNumber', 'roomStatus','createdAt', 'modifiedAt')
    list_display = ('building','floor', 'roomNumber', 'roomStatus','createdAt', 'modifiedAt')


@admin.register(Floor)

class FloorModel(admin.ModelAdmin):
    list_filter =('building','floorNumber','createdAt', 'modifiedAt')
    list_display = ('building','floorNumber','createdAt', 'modifiedAt')


@admin.register(Tenant)

class TenantModel(admin.ModelAdmin):
    list_filter =('building','floor', 'room','name','payment','createdAt', 'modifiedAt')
    list_display = ('building','floor', 'room','name','payment', 'createdAt', 'modifiedAt')

@admin.register(Rental)

class RentalModel(admin.ModelAdmin):
    list_filter =('building','floor', 'room','rentalAmount','createdAt', 'modifiedAt')
    list_display = ('building','floor', 'room','rentalAmount','createdAt', 'modifiedAt')

    
@admin.register(Comments)
    
class CommentsModel(admin.ModelAdmin):
    list_filter =('building','floor', 'room','comment','createdAt', 'modifiedAt')
    list_display = ('building','floor', 'room','comment','createdAt', 'modifiedAt')

