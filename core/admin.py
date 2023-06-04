from django.contrib import admin

from core.models import *
# Register your models here.

@admin.register(Building)

class BuildingModel(admin.ModelAdmin):
    list_filter =('buildingName', 'city' , 'createdAt')
    list_display = ('buildingName' , 'city', 'createdAt')
    

@admin.register(Room)

class RoomModel(admin.ModelAdmin):
    list_filter =('building','floor', 'roomNumber', 'roomStatus','createdAt')
    list_display = ('building','floor', 'roomNumber', 'roomStatus','createdAt')


@admin.register(Floor)

class FloorModel(admin.ModelAdmin):
    list_filter =('building','floorNumber','createdAt')
    list_display = ('building','floorNumber','createdAt')


@admin.register(Tenant)

class TenantModel(admin.ModelAdmin):
    list_filter =('building','floor', 'room','name','payment','createdAt', 'modifiedAt')
    list_display = ('building','floor', 'room','name','payment', 'createdAt', 'modifiedAt')

@admin.register(Rental)

class RentalModel(admin.ModelAdmin):
    list_filter =('building','floor', 'room','rentalAmount','createdAt')
    list_display = ('building','floor', 'room','rentalAmount','createdAt')

    
@admin.register(Comments)
    
class CommentsModel(admin.ModelAdmin):
    list_filter =('building','floor', 'room','comment','createdAt')
    list_display = ('building','floor', 'room','comment','createdAt')

@admin.register(Expense)
    
class ExpenseModel(admin.ModelAdmin):
    list_filter =('building','floor', 'room','expense','amount','createdAt')
    list_display = ('building','floor', 'room','expense','amount','createdAt')

# @admin.register(Expense2)
    
# class Expense2Model(admin.ModelAdmin):
#     list_filter =('building','floor', 'room','expense','amount','createdAt')
#     list_display = ('building','floor', 'room','expense','amount','createdAt')
