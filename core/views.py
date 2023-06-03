from rest_framework import serializers
from rest_framework import viewsets
from .serializer import * 
from .models import * 
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render 
from django.http import HttpResponse
from datetime import datetime
import calendar
from django.db.models import Sum


from django.db import connection
# Create your views here.

class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

def countOccupiedRooms():
    with connection.cursor() as cursor:
        
        # Append leading zero if current_month is less than 10
        current_month = datetime.now().month
        current_month = str(current_month).zfill(2)
        current_year = datetime.now().year 

        query = f"""
            SELECT COUNT(*) 
            FROM core_Room
            WHERE roomStatus = 'occupied'
            AND strftime('%m', modifiedAt) = '{current_month}'
            AND strftime('%Y', modifiedAt) = '{current_year}'
        """

        queryPaymentsMade = f"""
        SELECT count(payment) 
        FROM core_tenant
        WHERE strftime('%m', modifiedAt) = '{current_month}'
        AND strftime('%Y', modifiedAt) = '{current_year}'
        """

        queryTotalPaymentsMade = f"""
        SELECT SUM(payment) 
        FROM core_tenant
        WHERE strftime('%m', modifiedAt) = '{current_month}'
        AND strftime('%Y', modifiedAt) = '{current_year}'
        """

        queryNumberUnits = f"""
            SELECT COUNT(*) 
            FROM core_Room
            WHERE strftime('%m', modifiedAt) = '{current_month}'
            AND strftime('%Y', modifiedAt) = '{current_year}'
        """


        with connection.cursor() as cursor:
            cursor.execute(query)
            occupiedCount = cursor.fetchone()[0]

            cursor.execute(queryPaymentsMade)
            queryPaymentsMade = cursor.fetchone()[0]

            cursor.execute(queryTotalPaymentsMade)
            queryTotalPaymentsMade = cursor.fetchone()[0]

            cursor.execute(queryNumberUnits)
            queryNumberUnits = cursor.fetchone()[0]
        
        thisList = []
        thisList.append(occupiedCount)
        thisList.append(queryPaymentsMade)
        thisList.append(queryTotalPaymentsMade)
        thisList.append(queryNumberUnits)



    # return HttpResponse(f'Total comments: {occupiedCount}')
    # return occupiedCount
    return thisList


def home(request):

    # get the current name of the month 
    current_month = datetime.now().month
    month_name = calendar.month_name[current_month]

    # get the recent payments in descending order 
         # Limit the queryset to 5 objects
    recentPayments = Tenant.objects.order_by('-modifiedAt')[:5]

    context = {
        
        'month_name' : month_name,
        'occupiedRooms' : countOccupiedRooms()[0],
        'paymentsMade' : countOccupiedRooms()[1],
        'totalPayments' : countOccupiedRooms()[2],
        'totalUnitNumber' : countOccupiedRooms()[3], 
        'tenants' : recentPayments,
        'expenses' : Expense.objects.all(),
        # get total of expenses 
        'totalExpenses' : Expense.objects.aggregate(total=Sum('amount'))['total']
        
    }
    return render(request, 'core/home.html', context)


def index(request):

    # get the current name of the month 
    current_month = datetime.now().month
    month_name = calendar.month_name[current_month]
    
    context = {
        
        'month_name' : month_name,
        'occupiedRooms' : countOccupiedRooms()[0],
        'paymentsMade' : countOccupiedRooms()[1],
        'totalPayments' : countOccupiedRooms()[2],
        'totalUnitNumber' : countOccupiedRooms()[3], 
    }
    return render(request, 'core/index.html', context)

