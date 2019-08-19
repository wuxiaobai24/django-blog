
import frontmatter
import os
import django
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

django.setup()

from blog.models import *

author = User.objects.get(id=1)
print(author)

def parsetime(s):
	s = s.split(' ')[0].split('-')
	return datetime(year=int(s[0]),
					month=int(s[1]),
					day=int(s[2]))

def create_post(path):
	with open(path) as f:
		md = frontmatter.load(f)
		title = md.get('title', default='No Title')
		if title is None:
			title = 'No Title'
		body = md.content
		created_time = md.get('date')
		print(created_time)
		# if created_time:
		# 	created_time = parsetime(created_time)

		# category_name = md.get('categories')
		#category = None
		
		category = Category.objects.get_or_create(name='编程')[0]
		
		taglist = md.get('tags')
		tags = None
		if taglist and len(taglist) != 0:
			tags = []
			for tag in taglist:
				tags.append(Tag.objects.get_or_create(name=tag)[0])
		dic = {
			'title': title,
			'body': body,
			'created_time': created_time if created_time else datetime.now(),
			'author': author,
			'category': category
		}
		# if category:
		# 	dic['category'] = category
		
		
		p = Post(**dic)	
		print(p.created_time)
		p.save()
		if tags:
			for tag in tags:
				p.tags.add(tag)
			p.save()
		# Post.objects.create()
inputpath = '/home/wuxiaobai24/code/python/postloader/posts/'
filepath = inputpath + '加一.md'
if __name__ == '__main__':
	Post.objects.all().delete()
	Tag.objects.all().delete()
	Category.objects.all().delete()

	for path in os.listdir(inputpath):
		print(path)
		create_post(os.path.join(inputpath, path))