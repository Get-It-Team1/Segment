from django.shortcuts import render
from .models import Card

# Create your views here.
def index(request):
    cards = Card.objects.all()

    return render(
        request,
        'blog/index.html',
        {
            'cards': cards,
        }
    )