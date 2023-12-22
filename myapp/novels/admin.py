from django.contrib import admin

# Register your models here.
# from novels.admin import CategoryAdmin, ChapterAdmin, NovelAdmin
from .models import *


class NovelAdmin(admin.ModelAdmin):
    fields = ["title", "published_date", "year", "status", "category"]
    list_display = ["title", "published_date", "year", "status", "display_category"]
    def display_category(self, obj):
        return obj.category.name if obj.category else None

    # def published_recently(self, obj):
    #     return obj.was_published_recently()
    # published_recently.boolean = True
    # published_recently.short_description = "Published recently?"
    # list_filter = ("status", "category")
    # search_fields = ("title", "category__name")
    # date_hierarchy = "published_date"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ("name",)


class ChapterAdmin(admin.ModelAdmin):
    list_display = ["title", "content"]
    search_fields = ["title", "content"]


admin.site.register(Novel,NovelAdmin)
admin.site.register(Category)
admin.site.register(Chapter,ChapterAdmin)
