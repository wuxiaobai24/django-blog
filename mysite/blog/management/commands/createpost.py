from django.core.management.base import BaseCommand, CommandError
from blog.models import Post, Category, Tag, User
from django.utils import timezone
from ._private import *

class Command(BaseCommand):
	help = "Create Post by parse markdown file with front matter."

	def add_arguments(self, parser):
		parser.add_argument('path', nargs='*', type=str)
		parser.add_argument('--toml', action='store_true', help='front matter is TOML (defautl is YAML).')
		parser.add_argument('--dir', action='store_true', help='path is dir (default is markdown file).')

	def create_post(self, *args, **options):
		author = User.objects.get(id=1)
		for path in options['path']:
			md = ParseMarkdownFile(path, options['toml'])

			if md.get('date') is None:
				md.metadata['date'] = timezone.now()
			if md.get('categories') is None:
				md.metadata['categories'] = '编程'
			category = Category.objects.get_or_create(name=md.get('categories'))[0]

			dic = {
				'title': md.get('title', default='No Title'),
				'body': md.content,
				'created_time': md.metadata['date'],
				'author': author,
				'category': category,
			}

			p = Post(**dic)
			p.save()
			if md.get('tags'):
				for tagname in md.metadata['tags']:
					tag = Tag.objects.get_or_create(name=tagname)[0]
					p.tags.add(tag)
				p.save()

	def handle(self, *args, **options):
		if options['dir']:
			import os
			dirpath = options['path'][0]
			options['path'] = [os.path.join(dirpath, path) for path in os.listdir(dirpath)]
			print(options)
			self.create_post(*args, **options)
		else:
			self.create_post(*args, **options)