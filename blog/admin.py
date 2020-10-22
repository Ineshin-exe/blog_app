from django.contrib import admin

from blog.models import Post, Blog


class BlogAdmin(admin.ModelAdmin):
    model = Blog
    ordering = ('-id', )
    list_display = ('author', )


class PostAdmin(admin.ModelAdmin):
    model = Post
    ordering = ('-created', 'title', )
    list_display = ('title', 'blog', )


admin.site.register(Blog, BlogAdmin)
admin.site.register(Post, PostAdmin)
