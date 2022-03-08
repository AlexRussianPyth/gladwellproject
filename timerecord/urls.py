from django.urls import path
from .views import homepage_view, set_goal_view, goal_detail_view, GoalCreateView
from django.conf.urls.static import static
from django.conf import settings

app_name = "timerecord"

urlpatterns = [
    path("", homepage_view, name="homepage"),
    path("set-goal", set_goal_view, name="set-goal"),
    path("goal/<slug:slug>", goal_detail_view, name="goal-detail"),
    path("create", GoalCreateView.as_view(), name="goal-create"), # через вьюшку-класс
    # path("slug:slug", set_goal_view, name="goal-detail"), # TODO
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)