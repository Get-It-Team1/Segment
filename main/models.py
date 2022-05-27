from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/main/tag/{self.slug}/'  

class Review(models.Model):
    #서평 제목
    title = models.CharField(max_length=30)
    #서평 본문
    content = models.TextField()
    #책 표지
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    #작성자
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    #해시태그
    tags = models.ManyToManyField(Tag, blank=True)

    #작성일
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #좋아요
    like = models.IntegerField(default=0)

    def __str__(self):
        return f'[{self.pk}]{self.title}::{self.author}'

    def get_absolute_url(self):
        return f'/{self.pk}'
  
class Experience(models.Model):
    #체험단 제목
    title = models.CharField(max_length=30)
    #체험단 본문
    content = models.TextField()
    #책 표지
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    #작성자
    author = None
    

    #작성일
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'[{self.pk}]{self.title}::{self.author}'

    def get_absolute_url(self):
        return f'/{self.pk}'