from django import forms
from .models import Profile, Task


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("name", "bio", "avatar")


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("title", "description", "is_done", "category", "tags")