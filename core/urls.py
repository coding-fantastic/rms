from django.urls import path, include 
from .views import TenantViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

router.register('Tenant', TenantViewSet, basename='Tenant')
router.register('Comments', CommentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index),
    # path('comments/count/', views.count_comments, name='count_comments'),
    path('home',views.home,),
]
