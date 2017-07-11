from django.contrib import admin
from rango.models import Category, Page, UserProfile


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'views', 'likes', 'slug')


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'views')


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'website', 'picture')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
