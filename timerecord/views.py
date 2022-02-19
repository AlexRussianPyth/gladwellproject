from django.shortcuts import render, redirect
from .models import Goal
from .forms import GoalForm
from .utils import handle_uploaded_file
from django.http import HttpResponse, HttpResponseRedirect 
# Create your views here.

def homepage_view(request):

    all_objects = Goal.objects.all()

    context = {
        "all_objects" : all_objects
    }

    return render(request, 'timerecord/homepage.html', context)

def set_goal_view(request):

    form = GoalForm()

    context = {
        "form" : form
        }

    if request.method == "POST":
        form = GoalForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES['image'])
            form.save()
            return redirect('homepage')
        else:
            raise Exception("Форма невалидна")
     
    return render(request, 'timerecord/setgoal.html', context)