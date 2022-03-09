from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import redirect


# Create your views here.

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("accounts:user-login")
    return render(request, "accounts/register.html", {"form" : form})

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