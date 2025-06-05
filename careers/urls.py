from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CareerModelViewSet
from .views import CommentViewSet


router = DefaultRouter()
router.register('careers', CareerModelViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]