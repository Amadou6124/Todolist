from django.views.generic import DeleteView, ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/task_list.html'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('-created_at')