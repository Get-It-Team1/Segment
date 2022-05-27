from pyexpat import model
from urllib import request
from django.shortcuts import render
from .models import Experience, Review, Category
from django.views.generic import ListView, DetailView

# Create your views here.

    
def ReviewList(request):
    model = Review
    review_pk = Review.objects.all().order_by('-pk')[:18]
    review_like = Review.objects.all().order_by('-like')[:18]

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