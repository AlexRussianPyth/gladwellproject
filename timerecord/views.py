from django.shortcuts import get_object_or_404, render, redirect
from .models import Goal
from .forms import GoalForm
from .utils import handle_uploaded_file
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView
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

def goal_detail_view(request, slug):

    goal_object = get_object_or_404(Goal, slug=slug)
    context = {
        "goal_object" : goal_object
    }

    return render(request, 'timerecord/goal-detail.html', context)

class GoalCreateView(CreateView):
    # template_name = 'timerecord/create.html'
    model = Goal
    fields = '__all__'
    # success_url = ''

