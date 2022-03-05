from django.urls import path
from .views import homepage_view, set_goal_view, goal_detail_view

app_name = "timerecord"

urlpatterns = [
    path("", homepage_view, name="homepage"),
    path("set-goal", set_goal_view, name="set-goal"),
    path("goal/<slug:slug>", goal_detail_view, name="goal-detail"),
    # path("slug:slug", set_goal_view, name="goal-detail"), # TODO
]