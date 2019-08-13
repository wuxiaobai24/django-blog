from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage, PageNotAnInteger

from django.views import generic
from .models import Category, Tag, Post

import markdown
# Create your views here.

def get_tags():
    return Tag.objects.all();

def get_categories():
    return Category.objects.all();

def index(request):
    paginator = Paginator(Post.objects.all().order_by('-created_time'), 3)

    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except (InvalidPage, EmptyPage):
        post_list = paginator.page(paginator.num_pages)

    context = {
        'hero': True,
        
        'post_list': post_list,
        'tags': get_tags(),
        'categories': get_categories(),
    }

    return render(request, 'blog/index.html', context=context)


def post(request, id):
    post = get_object_or_404(Post, pk=id)
    ext = [
        'markdown.extensions.extra',
        # 'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ]
    post.clicks += 1
    post.save()
    post.body = markdown.markdown(post.body, extensions=ext, safe_mode=True)
    context = {
        'title': post.title,
        'post': post,
        'tags': get_tags(),
        'categories': get_categories(),
    }
    return render(request, 'blog/post.html', context=context)


def tag(request, id):
    tag = get_object_or_404(Tag, pk=id)
    paginator = Paginator(tag.get_posts().order_by('-created_time'), 3)

    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except (InvalidPage, EmptyPage):
        post_list = paginator.page(paginator.num_pages)

    context = {
        'title': 'Tags -- %s' % tag.name,
        'post_list': post_list,
        'tags': get_tags(),
        'categories': get_categories(),
    }

    return render(request, 'blog/index.html', context=context)

def category(request, id):
    category = get_object_or_404(Category, pk=id)
    paginator = Paginator(category.get_posts().order_by('-created_time'), 3)

    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except (InvalidPage, EmptyPage):
        post_list = paginator.page(paginator.num_pages)

    context = {
        'title': 'Category -- %s' % category.name,
        'post_list': post_list,
        'tags': get_tags(),
        'categories': get_categories(),
    }

    return render(request, 'blog/index.html', context=context)


def archives(request):
    paginator = Paginator(Post.objects.all().order_by('-created_time'), 10)

    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except (InvalidPage, EmptyPage):
        post_list = paginator.page(paginator.num_pages)

    context = {
        'hero': False,
        'title': 'Archives',
        'post_list': post_list,
        'tags': get_tags(),
        'categories': get_categories(),
    }

    return render(request, 'blog/archives.html', context=context)    


def about(request):
    return render(request, 'blog/index.html', context={'title': 'about'})
