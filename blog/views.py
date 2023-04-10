# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post,Category

# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-pk'
    # template_name = 'blog/post_list.html'

    # 'blog/post_list.html' : class 이름_list.html 은 내부적으로 정의가 되어있기때문에 생략 가능

    def get_context_data(self, **kwargs):
        context = super(PostList,self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

class PostDetail(DetailView):
    model = Post
    # template_name = 'blog/post_detail.html'
    
def single_post_page(request,pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
        'post' : post,
        
        }
    )
