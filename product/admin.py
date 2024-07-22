from django.contrib import admin
from product.models import Product, Variation
from . import models


class VariationInline(admin.TabularInline):
    model = models.Variation
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        VariationInline
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation)
