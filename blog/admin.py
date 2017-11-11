from django.contrib import admin
from .models import Post

# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','published_date']
    actions = ['make_published']
    def make_published (modeladmin, request , queryset):
        for post in queryset:
            post.publish()
    make_published.short_description = 'publicar'        


    