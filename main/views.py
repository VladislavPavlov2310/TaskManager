from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, ListView, DeleteView
from .models import Task
from .forms import TaskForm


class TaskListView(ListView):
    template_name = 'main/index.html'
    queryset = Task.objects.order_by('-id')
    context_object_name = 'tasks'


class TaskCreateView(CreateView):
    template_name = 'main/create.html'
    form_class = TaskForm
    queryset = Task.objects.all()

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('home')


class TaskDeleteView(DeleteView):
    model = Task

    def get_success_url(self):
        return reverse_lazy('home')


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'main/update.html'

    # def post(self, request, *args, **kwargs):
    #     form = self.get_form()
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('home')


def about(request):
    return render(request, 'main/about.html')
