from django.contrib import admin
from .models import Post, Category
# from django_summernote.admin import SummernoteModelAdmin
# from .models import SomeModel
# from django_summernote.admin import SummernoteModelAdmin
# from .models import Post

# Register your models here.

# Apply summernote to all TextField in model.
# summernote 관련 라이브러리
# class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
#     summernote_fields = '__all__'
# admin.site.register(SomeModel, SomeModelAdmin)

# #summernote 관련 
# class PostAdmin(SummernoteModelAdmin):
#     summernote_fields = ('content',)
# admin.site.register(Post, PostAdmin)

# Category 모델
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,CategoryAdmin)

