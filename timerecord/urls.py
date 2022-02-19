from django.urls import path
from .views import homepage_view, set_goal_view

urlpatterns = [
    path("", homepage_view, name="homepage"),
    path("set-goal", set_goal_view, name="set-goal"),
]