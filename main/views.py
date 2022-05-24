from pyexpat import model
from urllib import request
from django.shortcuts import render
from .models import Review
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

