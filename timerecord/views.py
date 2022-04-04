from django.shortcuts import get_object_or_404, render, redirect
from .models import Goal, Category
from .forms import GoalForm
from .utils import handle_uploaded_file
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
# Create your views here.

def homepage_view(request):
    context = {}
    print(request.user.is_authenticated)
    # if request.user.is_authenticated:
    #     user_goals = Goal.objects.filter(user=request.user)
    #     context['all_objects'] = user_goals
    # else:
    #     context['message'] = "Here could be your goals!"


    return render(request, 'timerecord/homepage.html', context)


# def goal_search(request):
    # qs = Article.objects.search(query)

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

@login_required
def goal_detail_view(request, slug):
    """Return Details of specific goal, all categories and timerecords"""

    goal_object = get_object_or_404(Goal, slug=slug)
    category_set = goal_object.category_set.all()

    timerecords = []
    for i, category in enumerate(category_set):
        timerecords.append([category, category.get_timerecords()])
    
    context = {
        "goal_object" : goal_object,
        "timerecords" : timerecords,
    }

    return render(request, 'timerecord/goal-detail.html', context)

class GoalCreateView(CreateView):
    # template_name = 'timerecord/create.html'
    model = Goal
    fields = '__all__'
    # success_url = ''

@login_required
def add_time_view(request, category_id):
    if request.method == "POST":
        minutes = request.POST.get("time_added")
        category = Category.objects.get(pk=category_id)
        category.add_timerecord(minutes=minutes)
        print("Время добавлено")
        return redirect(request.META.get('HTTP_REFERER'))

    return redirect("timerecord:homepage")