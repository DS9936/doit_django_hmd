from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from .models import Post,Category,Tag
from django.core.exceptions import PermissionDenied

# tag 를 가져온다
from django.utils.text import slugify


# Create your views here.





# 포스트크리에잇
class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title','hook_text','content','head_image','file_upload','category']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user

            # tags 추가
            response = super(PostCreate, self).form_valid(form)
            tags_str = self.request.POST.get('tags_str')
            if tags_str :
                tags_str = tags_str.strip()
                tags_str = tags_str.replace(',',';')
                tags_list = tags_str.split(';')

                for t in tags_list:
                    t = t.strip()
                    tag, is_tag_created = Tag.objects.get_or_create(name=t)
                    if is_tag_created:
                        tag.slug = slugify(t, allow_unicode=True)
                        tag.save()
                    self.object.tags.add(tag)
            return response
        
        else:
            return redirect('/blog/')

# 포스트리스트
class PostList(ListView):
    model = Post
    ordering = '-pk'
    
    # 한 page에 보여줄 목록 갯수 = paginate_by
    paginate_by = 3

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

# 포스트 서치
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

# 포스트수정페이지
class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title','hook_text','content','head_image','file_upload','category','tags']
    # UpdateView 상속 못받게 이름 지정
    template_name = 'blog/post_update_form.html'

    #dispatch 로 요청방식 판단하기
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else :
            raise PermissionDenied


# 내부페이지
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

