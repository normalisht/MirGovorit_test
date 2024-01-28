from django.contrib import admin
from .models import Recipe, Product


class ProductInline(admin.TabularInline):
    model = Recipe.products.through
    verbose_name = "Продукт"
    verbose_name_plural = "Продукты"
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    exclude = ("products",)
    inlines = (ProductInline,)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Product)
