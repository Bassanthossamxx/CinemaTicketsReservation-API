
from django.contrib import admin
from django.urls import path
from tickets import views

urlpatterns = \
    [
    path('admin/', admin.site.urls),
    #model And No Rest Framework
    path('UsingModelNoRest/',views.FBV_Model_No_Rest),
    #FBVs & Rest Framework
    path('rest/guests/',views.FBV_Get_Post_Guest), #Get and Post
    path('rest/guest/<int:pk>/' , views.FBV_Get_Put_Delete_Guest) #delete , update , get using ID
    ]
