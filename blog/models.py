from cgitb import text
from ctypes.wintypes import tagMSG
from django.db import models

# Create your models here.
class Card(models.Model):
    #서평 제목
    title = models.CharField(max_length=30)

    #책 정보
    book = models.CharField()

    #서평 본문
    text = models.CharField()

    #해시태그
    
    #카테고리

    #작성일
    created_at = models.DateField()

    #좋아요
    like = models.IntegerField()



class Book(models.Model):
    #책 제목
    title = models.CharField()

    #책 표지
    cover = models.ImageField()

    #저자
    author = models.CharField()