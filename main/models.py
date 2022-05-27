from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=50, unique = True)
    slug = models.SlugField(max_length=200, unique = True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/category/{self.slug}/'
    #SW교육에서는 경로가 blog/category인데 main/category로 바꿨어

    class Meta:
        verbose_name_plural='Categories'

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/tag/{self.slug}/'  

class Review(models.Model):
    #서평 제목
    title = models.CharField(max_length=30)
    #서평 본문
    content = models.TextField()
    #책 표지
    head_image = models.ImageField(upload_to='main/images/%Y/%m/%d/', blank=True)
    #작성자
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    #해시태그
    tags = models.ManyToManyField(Tag, blank=True)
    #카테고리
    category = models.ForeignKey(Category ,null=True, on_delete=models.SET_NULL, blank=True)

    #작성일
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #좋아요
    like = models.ManyToManyField(User, related_name='likes', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'[{self.pk}]{self.title}::{self.author}'

    def get_absolute_url(self):
        return f'/{self.pk}/'
    
    def get_like_url(self):
        return f'/{self.pk}/like/'
  
class Experience(models.Model):
    #체험단 제목
    title = models.CharField(max_length=30)
    #체험단 본문
    content = models.TextField()
    #책 표지
    head_image = models.ImageField(upload_to='main/images/%Y/%m/%d/', blank=True)
    #작성자
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    

    #작성일
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'[{self.pk}]{self.title}::{self.author}'

    def get_absolute_url(self):
        return f'/{self.pk}'

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author}::{self.content}'

    def get_absolute_url(self):
        return f'{self.review.get_absolute_url()}#comment-{self.pk}'