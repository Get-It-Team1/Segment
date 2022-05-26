from django.db import models
from django.contrib.auth.models import User
import os

author = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)

class Review(models.Model):
    #서평 제목
    title = models.CharField(max_length=30)
    #서평 본문
    content = models.TextField()
    #책 표지
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    #작성자
    author = None
    #해시태그
    
    #카테고리

    #작성일
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #좋아요
    like = models.IntegerField()

    def __str__(self):
        return f'[{self.pk}]{self.title}::{self.author}'

    def get_absolute_url(self):
        return f'/{self.pk}'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    #작성일
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'[{self.pk}]{self.title}::{self.author}'

    def get_absolute_url(self):
        return f'/{self.pk}'

