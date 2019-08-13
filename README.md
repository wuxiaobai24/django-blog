# django-blog

## 起源

由于嫌弃Hexo渲染太慢，Hugo模版太少（一直没有看到满意的），所以决定自己撸一个blog，于是就有了这个Repo。

为了快速开发，选择了`Django`作为后端，并使用`mdedtior`作为后台的Markdown编辑器，这部分基本没花多少时间。每次撸网站花的最多的时间就是前端部分了，这次抛弃了使用`bootstrap`的想法（实在是太繁琐了），选择了`bulma`作为CSS框架。因为博客的页面比较简单，所以不需要太多js，而且`bulma`已经非常丰富了，所以花了一天左右的时间学习了一下`Bulma`的东西，并实现了前端部分的`Demo`。打算部署完，在记录一下这次学习到的东西。

## 安装

1. 下载源码 

```bash
git clone https://github.com/wuxiaobai24/django-blog.git
```

2. 安装依赖

使用`pip`安装依赖

```bash
pip install -r requirements.txt
```

或者使用`pipenv`安装依赖

```bash
pipenv install -r requirements.txt
```

## 使用

```bash
python mysite/manage.py runserver 
```

## 项目结构

```
.
├── LICENSE
├── mysite
│   ├── blog
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── 0002_auto_20190810_1755.py
│   │   │   ├── 0003_post_clicks.py
│   │   │   ├── 0004_auto_20190813_2004.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── static
│   │   │   └── blog
│   │   │       ├── css
│   │   │       │   ├── bulma-badge.min.css
│   │   │       │   ├── bulma.min.css
│   │   │       │   ├── bulma-timeline.min.css
│   │   │       │   ├── github.css
│   │   │       │   ├── monokai.css
│   │   │       │   ├── style.css
│   │   │       │   └── typo.css
│   │   │       └── js
│   │   │           ├── highlight.pack.js
│   │   │           └── main.js
│   │   ├── templates
│   │   │   └── blog
│   │   │       ├── archives.html
│   │   │       ├── base.html
│   │   │       ├── _categories.html
│   │   │       ├── _footer.html
│   │   │       ├── _header.html
│   │   │       ├── _hero.html
│   │   │       ├── index.html
│   │   │       ├── _navbar.html
│   │   │       ├── post.html
│   │   │       └── _tags.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── db.sqlite3
│   ├── manage.py
│   ├── mysite
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── uploads
│       └── editor
├── Pipfile
├── Pipfile.lock
├── READMD.md
├── requirements.txt
└── tree.txt

12 directories, 43 files
```

## License

[MIT](https://choosealicense.com/licenses/mit/)