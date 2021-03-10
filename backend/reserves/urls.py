# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

from reserves import views

router = DefaultRouter()
router.register(r'reserve', views.ReserveViewSet, basename='reserve')

urlpatterns = [
    path('', include(router.urls))]