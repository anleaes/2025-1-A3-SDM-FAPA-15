from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectMaterialViewSet

app_name = 'projectmaterial'

router = DefaultRouter()
router.register('', ProjectMaterialViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
