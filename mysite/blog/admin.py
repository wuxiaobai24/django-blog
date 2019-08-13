from django.contrib import admin

from .models import Category, Tag, Post
# Register your models here.


# class TagInline(admin.TabularInline):
#     model = Tag
#     extra = 1


# class CategoryInline(admin.StackedInline):
#     model = Category
#     extra = 1


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'author', ]}),
        ('Date information', {'fields': [
            'created_time', 'modified_time']}),
        ('Content', {'fields': ['body']}),
        ('Category', {'fields': ['category']}),
        ('Tags', {'fields': ['tags']}),
    ]
    # inlines = [CategoryInline, TagInline]
    list_display = ('title', 'created_time')
    list_filter = ['tags', 'category', 'created_time']
    search_fields = ['title']


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
