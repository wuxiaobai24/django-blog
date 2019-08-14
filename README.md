# django-blog

## 起源

由于嫌弃Hexo渲染太慢，Hugo模版太少（一直没有看到满意的），所以决定自己撸一个blog，于是就有了这个Repo。

为了快速开发，选择了`Django`作为后端，并使用`mdedtior`作为后台的Markdown编辑器，这部分基本没花多少时间。每次撸网站花的最多的时间就是前端部分了，这次抛弃了使用`bootstrap`的想法（实在是太繁琐了），选择了`Bulma`作为CSS框架。因为博客的页面比较简单，所以不需要太多js，而且`Bulma`已经非常丰富了，所以花了一天左右的时间学习了一下`Bulma`的东西，并实现了前端部分的`Demo`。打算部署完，在记录一下这次学习到的东西。

## 安装

1. 下载源码 

```bash
git clone https://github.com/wuxiaobai24/django-blog.git
```

2. 使用`virtualenv`或`pipenv`安装依赖

- `virtualenv`

``` bash
virtualenv venv -p python3.5
source venv/bin/activate
pip install -r requirements.txt
```

- `pipenv`

```bash
pipenv --python python3.5
pipenv install
```

## 使用

### 运行

```bash
source venv/bin/activate # 进入虚拟环境
# 使用pipenv则使用`pipenv shell`来进入虚拟环境
python mysite/manage.py runserver 
```

### 部署

1. 设置环境变量

   - `SECRET_KEY`：秘钥
   - `HOST`：IP地址

   **在`mysite/mysite/settings.py`中直接修改也可以**

2. 使用`collectstatic`命令收集静态文件：

   ```bash
   python mysite/manage.py collectstatic
   ```

3. 配置uwsgi.ini

4. 启动uwsgi

```bash
uwsgi --ini uwsgi.ini
# 确保没问题后使用`screen`后台运行uwsgi.ini
screen uwsgi --ini uwsgi.ini
```

4.启动`Nginx`

- 安装`Nginx`

```bash
# ubuntu
sudo apt-get install nginx
# arch
sudo pacman -S nginx
```

- 配置`Nginx`

`/etc/nginx/conf.d/www.example.com.conf`

```nginx
server {
	listen 80;
	server_name www.example.com;
	charset utf-8;
	
	client_max_body_size 75M;
	
	location /static {
		alias /project/django-blog/mysite/staticfiles; # 地址为静态文件所在的地址
	}
	
	location /media {
		alias /project/django-blog/mysite/media;
	}
	
	location {
		uwsgi_pass 127.0.0.1:8000;
		include /etc/nginx/uwsgi_params;
	}
}
```

`/etc/nginx/nginx.conf`

```nginx
# 在http的最后面添加`include /etc/nginx/conf.d/*.conf;`

http {
	# somthing....
	include /etc/nginx/conf.d/*.conf;	
}
```

- 重启`Nginx`

```bash
sudo systemctl restart nginx
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
├── README.md
├── requirements.txt
└── uwsgi.ini

12 directories, 43 files
```

## License

[MIT](https://choosealicense.com/licenses/mit/)