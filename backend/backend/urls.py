from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('oficinas.urls', 'office'), namespace='office')),
    path('', include(('reserves.urls', 'reserve'), namespace='reserve')),
]
