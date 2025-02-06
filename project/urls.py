from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tickets import views
from tickets.views import GuestViewSet, MovieViewSet, ReservationViewSet

# Import Swagger libraries
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Default Router
router = DefaultRouter()
router.register(r'guests', GuestViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'reservations', ReservationViewSet)

# Swagger Schema View
schema_view = get_schema_view(
    openapi.Info(
        title="Ticket Reservation API",
        default_version="v1",
        description="API documentation for managing guests, movies, and reservations.",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# URL Patterns
urlpatterns = [
    path('admin/', admin.site.urls),

    # Model And No Rest Framework
    path('UsingModelNoRest/', views.FBV_Model_No_Rest),

    # FBVs & Rest Framework
    path('FBV/guests/', views.FBV_List_Guest),  # Get and Post for guests
    path('FBV/movies/', views.FBV_List_Movie),  # Get and Post for movies
    path('FBV/reservations/', views.FBV_List_Reservation),
    path('FBV/guest/<int:pk>/', views.FBV_PK_Guest),
    path('FBV/movie/<int:pk>/', views.FBV_PK_Movie),
    path('FBV/reservation/<int:pk>/', views.FBV_PK_Reservation),

    # Default CBVs
    path('CBV/guests/', views.CBV_List_Guest.as_view()),
    path('CBV/guest/<int:pk>/', views.CBV_PK_Guest.as_view()),

    # Viewsets
    path('api/', include(router.urls)),

    # Swagger Documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # Swagger JSON for Postman
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
