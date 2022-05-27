
from re import L
from typing import List
from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from requests import RequestException
from .models import Review, Experience, Tag, Category
from pyexpat import model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.utils.text import slugify
#from .forms import CommentForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

# Create your views here.
    
def ReviewList(request):
    model = Review
    review_pk = Review.objects.all().order_by('-pk')[:18]
    review_like = Review.objects.all().order_by('-like_count')[:18]

    def get_context_data(self,**kwargs):
        context = super(ReviewList,self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Review.objects.filter(category = None).count()
        return context

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

    def get_context_data(self,**kwargs):
        context = super(ReviewDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Review.objects.filter(category = None).count()
        return context

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

def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        review_list = Review.objects.filter(category=None)
    else :
        category = Category.objects.get(slug=slug)
        review_list = Review.objects.filter(category=category)

    return render(
        request,
        'main/category.html',
        {
            'review_list': review_list,
            'categories': Category.objects.all(),
            'no_category_review_count': Review.objects.filter(category=None).count(),
            'category': category,
        }
    )


def user_page(request):
    review_list = Review.objects.filter(author= '1')

    return render(
        request,
        'main/user_blog.html',
        {
            'review_list': review_list,
        }
    )

def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    review_list = tag.review_set.all()

    return render(
        request,
        'main/tag_list.html',
        {
            'review_list':review_list,
            'tag':tag,
        }
    ) 

def likes(request, pk):
    like_b = get_object_or_404(Review, pk=pk)
    if request.user in like_b.like.all():
        like_b.like.remove(request.user)
        like_b.like_count -= 1
        like_b.save()
    else:
        like_b.like.add(request.user)
        like_b.like_count += 1
        like_b.save()
    return redirect('/'+str(pk)+'/')
