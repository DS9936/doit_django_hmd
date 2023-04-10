from django.urls import path
from .import views

urlpatterns =[
    #blog
    # 이부분은 차후에 채우겠다.
    #카테고리 페이지
    path('create_post/', views.PostCreate.as_view()),
    path('tag/<str:slug>/', views.tag_page),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views. PostList.as_view()),
    # path('', views.index),
]