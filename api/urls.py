from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoModelViewSet

router = DefaultRouter()
router.register(r'todos', TodoModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
