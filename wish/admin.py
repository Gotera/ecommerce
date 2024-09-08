from django.contrib import admin
from . import models


class InlineWishItem(admin.TabularInline):
    model = models.WishItem
    extra = 1


class AdminWish(admin.ModelAdmin):
    inlines = [
        InlineWishItem
    ]


admin.site.register(models.Wish, AdminWish)
admin.site.register(models.WishItem)
