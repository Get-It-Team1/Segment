from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    #posts = Post.objects.all()
    #post작성 후 주석지우기
    

    return render(
        request, 
        'blog/index.html',
        #{
        #    'posts' :  posts,
        #}
    )