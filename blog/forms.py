from .models import Comment
from django import forms


# 코맨트 폼 구현
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)