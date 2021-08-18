from django.contrib import admin

from .models import NewsPost, Photo


class NewsPostAdmin(admin.ModelAdmin):
    list_display = [
            'title',
            'published_at',
        ]


admin.site.register(NewsPost, NewsPostAdmin)
admin.site.register(Photo)
