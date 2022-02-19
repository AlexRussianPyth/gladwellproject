from django.shortcuts import render
from .models import Goal
# Create your views here.

def homepage_view(request):

    all_objects = Goal.objects.all()
    
    context = {
        "all_objects" : all_objects
    }

    return render(request, 'timerecord/homepage.html', context)