from django.db import models
#author 필드 추가하기
from django.contrib.auth.models import User
import os

# Create your models here.
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
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}'
    
    #확장자 아이콘 나타내기
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)
    
    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]