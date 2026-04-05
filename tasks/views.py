from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ProfileForm, TaskForm
from .models import Profile, Task, Category


def home_page(request):
    return render(request, "tasks/home.html")


def profile_list(request):
    profiles = Profile.objects.all().order_by("id")
    query = request.GET.get("q")

    if query:
        profiles = profiles.filter(name__icontains=query)

    paginator = Paginator(profiles, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "query": query
    }
    return render(request, "tasks/profile_list.html", context)


@login_required
def profile_create(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save()
            return redirect("profile_detail", profile_id=profile.id)
    else:
        form = ProfileForm()

    return render(request, "tasks/profile_create.html", {"form": form})


def profile_detail(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    return render(request, "tasks/profile_detail.html", {"profile": profile})


def register_page(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_page")
    else:
        form = UserCreationForm()

    return render(request, "tasks/register.html", {"form": form})


def login_page(request):
    error = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            error = "Неверный логин или пароль"

    return render(request, "tasks/login.html", {"error": error})


def logout_page(request):
    logout(request)
    return redirect("home")


def task_list(request):
    tasks = Task.objects.all().order_by("id")
    return render(request, "tasks/task_list.html", {"tasks": tasks})


@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("task_detail", task_id=task.id)
    else:
        form = TaskForm()

    return render(request, "tasks/task_create.html", {"form": form})


def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, "tasks/task_detail.html", {"task": task})


def task_done(request):
    tasks = Task.objects.filter(is_done=True).order_by("id")
    return render(request, "tasks/task_done.html", {"tasks": tasks})


def tasks_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    tasks = Task.objects.filter(category=category).order_by("id")

    context = {
        "category": category,
        "tasks": tasks
    }
    return render(request, "tasks/tasks_by_category.html", context)

@login_required
def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_detail", task_id=task.id)
    else:
        form = TaskForm(instance=task)

    return render(request, "tasks/task_edit.html", {"form": form, "task": task})


@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.delete()
        return redirect("task_list")

    return redirect("task_detail", task_id=task.id)