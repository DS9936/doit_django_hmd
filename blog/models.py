from django.db import models
#author 필드 추가하기
from django.contrib.auth.models import User
import os

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode = True)

    #카테고리 추가
    def __str__(self):
        return self.name
    
    #뱃지만들기
    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/'

#카테고리 추가
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode = True)

    #카테고리 추가
    def __str__(self):
        return self.name
    
    #뱃지만들기
    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'
    
    #카테고리(s)의 이름 지정
    # class Meta:
    #     verbose_name_plural = 'Categories'

    

class Post(models.Model):
    title = models.CharField(max_length=30)
    # 요약문 필드
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()

    # 이미지 업로드
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # author 필드
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    # 카테고리 필드
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    # tag 필드
    tags = models.ManyToManyField(Tag, blank=True)


    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}'
    
    #확장자 아이콘 나타내기
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)
    
    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]
    


# 내부페이지의 comment 모델
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author}::{self.content}'
    
    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'