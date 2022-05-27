from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique = True)
    slug = models.SlugField(max_length=200, unique = True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'
    #SW교육에서는 경로가 blog/category인데 main/category로 바꿨어

    class Meta:
        verbose_name_plural='Categories'

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
    categroy = models.ForeignKey(Category ,null=True, on_delete=models.SET_NULL, blank=True)
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