from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
    path('core/', include('core.urls')),
    path('accounting/', include('accounting.urls')),
    path('pos/', include('pos.urls')),
    path('inventory/', include('inventory.urls')),
    path('restaurant/', include('restaurant.urls')),
    path('retail/', include('retail.urls')),
    path('car_dealership/', include('car_dealership.urls')),
]
