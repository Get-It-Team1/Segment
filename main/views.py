from re import L
from typing import List
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from requests import RequestException
from .models import Review, Experience, Tag
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.utils.text import slugify
#from .forms import CommentForm
from django.shortcuts import get_object_or_404

# Create your views here.

'''class ReviewList(ListView):
    model = Review
    ordering = '-pk'''
    
def ReviewList(request):
    review_pk = Review.objects.all().order_by('-pk')[:18]
    review_like = Review.objects.all().order_by('-like')[:18]

    return render(
        request,
        'main/review_list.html',
        {
            'review_pk' : review_pk,
            'review_like': review_like,
        }
    )


class ReviewDetail(DetailView):
    model = Review

class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Review
    fields = ['title', 'content', 'head_image']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/')


def ExperienceList(request):
    experinece_pk = Experience.objects.all().order_by('-pk')[:18]
    experinece_dueto = Experience.objects.all().order_by('created_at')[:18]

    return render(
        request,
        'main/Experience.html',
        {
            'experience_pk' : experinece_pk,
            'experience_dueto': experinece_dueto,
        }
    )

def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list':post_list,
            'tag':tag,
        }
    ) 