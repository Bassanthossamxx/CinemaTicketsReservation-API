
from django.contrib import admin
from django.urls import path

from tickets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ModelNoRest/',views.FBVModelNoRest),
]
