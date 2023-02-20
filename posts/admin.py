from django.contrib import admin

from posts.models import BlogPost

@admin.register(BlogPost)
class blogpost(admin.ModelAdmin):
    model = BlogPost
    list_display = [
        'title',
        'published',
        'last_updated',
        'created_on',
    ]

    list_editable = ['published']