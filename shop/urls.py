from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('products/', views.products),
    path('cart/add/', views.add_to_cart),
    path('cart/', views.cart),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('shop.urls')),
]