from django.urls import path, include
from rest_framework.routers import DefaultRouter
from careers.views import CareerModelViewSet

router = DefaultRouter()
router.register('careers', CareerModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]