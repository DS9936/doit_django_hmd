from django.urls import path
from .import views
from django.views.generic import TemplateView


urlpatterns =[
    path('single_pages/about_me.html', TemplateView.as_view(template_name='single_pages/about_me.html'), name='about_me'),
    path('', views.landing),

]