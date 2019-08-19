import frontmatter
from frontmatter.default_handlers import YAMLHandler, TOMLHandler

def ParseMarkdownFile(path, istoml):
	with open(path, 'r') as f:
		if istoml:
			md = frontmatter.load(f, handler=TOMLHandler())
		else:
			md = frontmatter.load(f, handler=YAMLHandler())
	return md