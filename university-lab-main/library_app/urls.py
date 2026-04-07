from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LibraryRecordViewSet

router = DefaultRouter()
router.register(r'records', LibraryRecordViewSet)

# This variable name MUST be exactly 'urlpatterns'
urlpatterns = [
    path('', include(router.urls)),
]