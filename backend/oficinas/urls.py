# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

from oficinas import views

router = DefaultRouter()
router.register(r'office', views.OfficeViewSet, basename='office')

urlpatterns = [
    path('', include(router.urls))]