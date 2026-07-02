from django.contrib import admin
from .models import Category, News, Comment
from .telegram_bot import send_to_telegram


admin.site.register(Category)
admin.site.register(Comment)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        is_new = obj.pk is None

        super().save_model(request, obj, form, change)

        if is_new:
            send_to_telegram(obj)