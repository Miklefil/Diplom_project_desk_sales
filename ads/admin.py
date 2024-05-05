from django.contrib import admin

from ads.models import Ad, Review


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'description', 'author', 'created_at', 'image')
    search_fields = ('title', 'price', 'author', )
    list_filter = ('author', 'created_at')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'author', 'ad', 'created_at')
    search_fields = ('id', 'author', 'ad', )
    list_filter = ('author', 'created_at', )
