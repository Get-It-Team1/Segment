from django.urls import path
from . import views
urlpatterns = [
    path('category/<str:slug>/', views.category_page),
    path('', views.ReviewList),
    path('<int:pk>/', views.ReviewDetail.as_view()),
    path('Experience/', views.ExperienceList),
]
