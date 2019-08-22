from django.contrib.syndication.views import Feed
from django.shortcuts import reverse

from .models import Post

class AllPostsRssFeed(Feed):
	title = 'Code & Fun'
	link = '/'
	description = "wuxiaobai24's blog"

	def items(self):
		# print('Feed', len(Post.objects.order_by('-created_time')))
		return Post.objects.order_by('-created_time')
	
	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.body

	def item_link(self, item):
		return reverse('blog:post',args=[item.id])