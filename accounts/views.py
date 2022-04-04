from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from timerecord.models import Goal
from .forms import AchieverForm
from django.contrib.auth.decorators import login_required



def register_view(request):
    """Shows a template with the form to create new user"""

    # if request.method == "POST":
    #     user_form = UserForm(request.POST)
    #     profile_form = ProfileForm(request.POST)
    #     if user_form.is_valid() and profile_form.is_valid():
    #         user_form.save()

    #         created_user = User.objects.get(username=request.POST.get("username"))

    #         print(created_user, type(created_user))

    #         # Profile.objects.create(
    #         #     user=created_user,
    #         #     photo=request.POST.get("photo"),
    #         #     about=request.POST.get("about"),
    #         #     )

    #         print("Сохранено")

    # user_form = UserForm()
    # profile_form = ProfileForm()

    return render(request, "accounts/register.html")




    # form = UserCreationForm(request.POST or None)

    # if request.method == "POST":
    #     print(request.POST.get("about"))
    #     print(request.POST.get("photo"))
    #     # form.save()
    #     return redirect("accounts:login")
        
    # return render(request, "accounts/register.html", {"form" : form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("timerecord:homepage")
    else:
        form = AuthenticationForm(request)

    context = {
        "form" : form
    }

    return render(request, "accounts/login.html", context=context)


def logout_view(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER'))
    # Redirect to a success page.

@login_required
def profile_view(request, username):
    current_user = request.user

    # user presses edit button
    if request.htmx:
        form = AchieverForm(instance=current_user)

        context = {
            'form' : form
            }

        return render(request, 'accounts/hx-userform.html', context)

    if current_user.is_authenticated:
        goals = Goal.objects.filter(user=current_user)

        context = {
            "goals" : goals
        }

        return render(request, "accounts/profile.html", context)
    print("User не залогирован")
    return redirect("accounts:login")

def test_view(request):
    return render(request, 'accounts/hx-test.html', context={})