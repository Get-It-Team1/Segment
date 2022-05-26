from django.urls import path
from . import views
urlpatterns = [
    path('', views.ReviewList),
    path('<int:pk>/', views.ReviewDetail.as_view()),
    path('Experience/', views.ExperienceList),
    path('tag/<str:slug>/', views.tag_page),
]
