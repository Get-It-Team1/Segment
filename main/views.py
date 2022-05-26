from pyexpat import model
from urllib import request
from django.shortcuts import render
from .models import Experience, Review, Tag
from django.views.generic import ListView, DetailView

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