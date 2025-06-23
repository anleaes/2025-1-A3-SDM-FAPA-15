from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectTypeViewSet

app_name = 'projecttype'

router = DefaultRouter()
router.register('', ProjectTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
