from django.urls import path
from .import views

urlpatterns =[
    #blog
    # 이부분은 차후에 채우겠다.
    #수정페이지
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    #카테고리 페이지
    path('search/<str:q>/', views.PostSearch.as_view()),
    path('create_post/', views.PostCreate.as_view()),
    path('tag/<str:slug>/', views.tag_page),
    path('category/<str:slug>/', views.category_page),

    # post_detail.html 에서 action="{{ post.get_absolute_url }}new_comment/"> 와 마찬가지로
    path('<int:pk>new_comment/', views.new_comment),
    
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views. PostList.as_view()),
    # path('', views.index),

]