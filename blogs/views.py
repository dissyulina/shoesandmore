from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_articles(request):
    """ Render all articles """

    blogs = Blog.objects.all().order_by('-created_on')

    context = {
        'blogs': blogs,
    }

    return render(request, 'blogs/articles.html', context)


def article_detail(request, blog_id):
    """ A view to show individual blog/article """

    blog = get_object_or_404(Blog, pk=blog_id)

    context = {
        'blog': blog,
    }

    return render(request, 'blogs/article.html', context)