from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from .models import Post,Category,Tag


# Create your views here.






class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title','hook_text','content','head_image','file_upload','category']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/blog/')

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

def category_page(request, slug):
    if slug == 'no_category' :
        category ='미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    # category = Category.objects.get(slug=slug)

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list' : post_list,
            'categories' : Category.object.all(),
            'no_category_post_count' : Post.object.filter(category=None).count(),
            'category' : category,
        }
    )

class PostSearch(PostList):
    paginate_by = None

    def get_queryset(self):
        q = self.kwargs['q']
        post_list = Post.objects.filter(
            Q(title__contains=q) | Q(tags__name__contains=q)
        ).distinct()
        return post_list

    def get_context_data(self, **kwargs):
        context = super(PostSearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'Search: {q}({self.get_queryset().count()})'

        return context



def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()

    return render(
        request,
        'blog/post_list.html',
        {
        'post_list': post_list,
        'tag' : tag,
        'categories' : Category.objects.all(),
        'no_category_post_count' : Post.objects.filter(category=None).count(),
        }
    )


class PostDetail(DetailView):
    model = Post
    # template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetail,self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

    
def single_post_page(request,pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
        'post' : post,
        
        }
    )
