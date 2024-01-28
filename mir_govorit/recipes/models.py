from django.db import models


class Product(models.Model):
    title = models.CharField(verbose_name="Название", max_length=128)
    cooking_counter = models.PositiveIntegerField(
        verbose_name="Кол-во приготовлений",
        default=0
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"


class Recipe(models.Model):
    title = models.CharField(verbose_name="Название", max_length=128)
    products = models.ManyToManyField(
        verbose_name="Продукты",
        to=Product,
        through="RecipeProducts"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"


class RecipeProducts(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    weight = models.PositiveIntegerField(verbose_name="вес (г)")

    def __str__(self):
        return (f"{self.product.title} {self.weight}г "
                f"(приготовлено: {self.product.cooking_counter})")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["product", "recipe"],
                name="unique_product_for_recipe"
            )
        ]
