from django.http import JsonResponse
from django.shortcuts import render
from .models import *

#We have types of Views :


# 1- Function Based View :
     # a- No model and No rest :
        # every table is an List of directory like this :
# guests = [
#     {'id': 1, 'name': 'Omar', 'mobile': 789456},
#     {'id': 2, 'name': 'Yassin', 'mobile': 74123}
# ]
        # then to output it change it to Json response and send to it the list of directory name to output it

# def FBVNoModelNoRest(request):
#     person =\
#         [
#         {'id': 1, 'name': 'Bav', 'mobile': 789456},
#         {'id': 2, 'name': 'Hossam', 'mobile': 74123},
#         ] #here you write data you need to output in manual way "list of directory"
#     return JsonResponse(person, safe=False) #change iot to json output to see it in url
        #then output it as url link it using urls.py in project

    # b-#2 model data default django without rest framework

def FBVModelNoRest(request):
    # Get all data from the Guest model
    data = Guest.objects.all()

    # Convert QuerySet to a list of dictionaries
    response = {
        'guests': list(data.values())  # Convert to list
    }

    return JsonResponse(response)  # No need to set safe=False unless needed

#ORM :
#list and create same view
# List == GET
# Create == POST
#pk query & update & delete same view
# pk query == GET >> using ID
# Update == PUT
# Delete destroy == DELETE





