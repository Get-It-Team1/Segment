from .models import Review
from django.views.generic import ListView, DetailView

# Create your views here.

class ReviewList(ListView):
    model = Review
    ordering = '-pk'
    

class ReviewDetail(DetailView):
    model = Review
