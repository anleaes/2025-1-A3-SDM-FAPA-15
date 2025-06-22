from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SupplierViewSet

app_name = 'supplier'

router = DefaultRouter()
router.register('', SupplierViewSet)

urlpatterns = [
    path('', include(router.urls)),
]