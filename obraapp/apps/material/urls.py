from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MaterialViewSet

app_name = 'material'

router = DefaultRouter()
router.register('', MaterialViewSet)

urlpatterns = [
    path('', include(router.urls)),
]