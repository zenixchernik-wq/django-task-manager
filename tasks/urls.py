from django.urls import path
from .views import *

urlpatterns = [
    path("", home_page, name="home"),

    path("register/", register_page, name="register_page"),
    path("login/", login_page, name="login_page"),
    path("logout/", logout_page, name="logout_page"),

    path("profiles/", profile_list, name="profile_list"),
    path("profile/create/", profile_create, name="profile_create"),
    path("profile/<int:profile_id>/", profile_detail, name="profile_detail"),

    path("tasks/", task_list, name="task_list"),
    path("task/create/", task_create, name="task_create"),
    path("task/<int:task_id>/", task_detail, name="task_detail"),
    path("tasks/done/", task_done, name="task_done"),
    path("tasks/category/<int:category_id>/", tasks_by_category, name="tasks_by_category"),

    path("task/<int:task_id>/edit/", task_edit, name="task_edit"),
    path("task/<int:task_id>/delete/", task_delete, name="task_delete"),
]