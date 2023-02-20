from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from posts.froms import BlogPostForm
from posts.models import BlogPost


class indexHome(ListView):
    model = BlogPost
    context_object_name = "posts"

    def get_queryset(self):
        query = super().get_queryset()
        if self.request.user.is_authenticated:
            return query
        return query.filter(published=True)


class indexCreate(CreateView):
    model = BlogPost
    fields = [
        "title",
        "content",
    ]
    context_object_name = 'form'
    success_url = reverse_lazy("home")


class indexUpdate(UpdateView):
    model = BlogPost
    fields = [
        "title",
        "content",
        "published",
    ]
    context_object_name = "update"
    success_url = reverse_lazy("home")


class indexDelete(DeleteView):
    model = BlogPost
    context_object_name = 'delete'
    success_url = reverse_lazy('home')


class indexDetail(DetailView):
    model = BlogPost
    template_name = 'detail.html'
    context_object_name = 'detail'
