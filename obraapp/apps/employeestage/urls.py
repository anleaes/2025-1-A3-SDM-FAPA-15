from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeStageViewSet

app_name = 'employeestage'

router = DefaultRouter()
router.register('', EmployeeStageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
