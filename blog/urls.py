from django.urls import path
from .import views

urlpatterns =[
    # 이부분은 차후에 채우겠다.
    path('<int:pk>/', views.single_post_page),
    path('', views.index),
    
]