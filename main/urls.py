from django.urls import path
from . import views
urlpatterns = [
    path('', views.ReviewList),
    path('<int:pk>/', views.ReviewDetail.as_view()),
]
