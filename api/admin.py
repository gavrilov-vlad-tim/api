from django.contrib import admin

from .models import Follow, Group, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['text', 'pub_date', 'author', 'group']


admin.site.register(Post, PostAdmin)
admin.site.register(Follow)
admin.site.register(Group)
