
from django.contrib import admin
from django.urls import path , include
from rest_framework.routers import DefaultRouter
from tickets import views
from tickets.views import GuestViewSet, MovieViewSet, ReservationViewSet

#we need to make default route to not repeat code :
router = DefaultRouter()
router.register(r'guests', GuestViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'reservations', ReservationViewSet)
urlpatterns = \
    [
    path('admin/', admin.site.urls),
    #model And No Rest Framework
    path('UsingModelNoRest/',views.FBV_Model_No_Rest),
    #FBVs & Rest Framework
    path('FBV/guests/',views.FBV_List_Guest), #Get and Post for guests
    path('FBV/movies/',views.FBV_List_Movie), #Get and Post for movies
    path('FBV/reservations/',views.FBV_List_Reservation),
    path('FBV/guest/<int:pk>/', views.FBV_PK_Guest),
    path('FBV/movie/<int:pk>/', views.FBV_PK_Movie),
    path('FBV/reservation/<int:pk>/', views.FBV_PK_Reservation),
    #Default CBVs
    path('CBV/guests/',views.CBV_List_Guest.as_view()),
    path('CBV/guest/<int:pk>/',views.CBV_PK_Guest.as_view()),
    #Viewsets
    path('api/', include(router.urls)),
        ]