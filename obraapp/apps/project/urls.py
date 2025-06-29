from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet

app_name = 'project'  

router = DefaultRouter()
router.register('', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]