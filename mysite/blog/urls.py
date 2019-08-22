from django.urls import path

from . import views
from .feeds import AllPostsRssFeed


app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('posts/<int:id>',views.post, name='post'),
    path('tags/<int:id>',views.tag, name='tag'),
    path('categories/<int:id>',views.category, name='category'),
    path('archives', views.archives,  name='archives'),
    path('atom.xml', AllPostsRssFeed(), name='rss')
    # path('archives/', views.archives, name='archives'),
    # path('about/', views.about, 'about')
]
