
from django.contrib import admin
from django.urls import path
from tickets import views

urlpatterns = \
    [
    path('admin/', admin.site.urls),
    #model And No Rest Framework
    path('UsingModelNoRest/',views.FBV_Model_No_Rest),
    #FBVs & Rest Framework
    path('rest/guests/',views.FBV_List_Guest), #Get and Post for guests
    path('rest/movies/',views.FBV_List_Movie), #Get and Post for movies
    path('rest/reservations/',views.FBV_List_Reservation), #Get and Post for reservations
    path('rest/guest/<int:pk>/', views.FBV_PK_Guest),  # delete , update , get using ID for guests
path('rest/movie/<int:pk>/', views.FBV_PK_Movie),  # delete , update , get using ID for movie
path('rest/reservation/<int:pk>/', views.FBV_PK_Reservation),  # delete , update , get using ID for reservation
    path('rest/reservation/movie/<int:pk>',views.FBV_Filter), #filter reservation to get all same movie reservations
path('rest/reservation/guest/<int:pk>',views.FBV_Filter) ,  #filter reservation to get all same guest reservations
    ]
