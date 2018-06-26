from django.contrib import admin
from .models import Post,NewPost,Comments
# Register your models here.
admin.site.register(Post)
admin.site.register(NewPost)
admin.site.register(Comments)