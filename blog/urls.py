from django.urls import path
from .import views

urlpatterns =[
    #blog
    # 이부분은 차후에 채우겠다.
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views. PostList.as_view()),
    # path('', views.index),
]