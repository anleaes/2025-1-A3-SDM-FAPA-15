from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet

app_name = 'employee'

router = DefaultRouter()
router.register('', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
