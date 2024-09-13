from django.contrib import admin
from django.urls import path, include
from ipo.views import home  # Import the home view
from rest_framework.routers import DefaultRouter
from ipo.views import IPOViewSet

router = DefaultRouter()
router.register(r'ipos', IPOViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', home),  # Add this line for the home page
]