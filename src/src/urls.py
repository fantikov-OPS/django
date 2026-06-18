from django.contrib import admin
from django.urls import path, include
from app.views import home, add_customer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('add/', add_customer, name='add_customer'),
    path('indexes/', include('app.urls')),
]
