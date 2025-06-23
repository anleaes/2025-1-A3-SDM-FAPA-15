from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StageViewSet

app_name = 'stage'  

router = DefaultRouter()
router.register('', StageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
