from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    """
    Admin settings to display list of Blogs
    """

    model = Blog
    list_display = (
        'title',
        'author',
        'image',
        'created_on',
        'paragraph1',
        'paragraph2',
        'paragraph3',
    )

    ordering = ('-created_on',)

admin.site.register(Blog, BlogAdmin)
