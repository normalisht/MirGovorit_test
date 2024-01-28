from http import HTTPStatus

from django.shortcuts import HttpResponse, get_object_or_404, render
from django.views.decorators.http import require_http_methods

from .models import Recipe, Product, RecipeProducts


@require_http_methods(["GET"])
def add_product_to_recipe(request):
    recipe_id = request.GET.get("recipe_id")
    product_id = request.GET.get("product_id")
    weight = request.GET.get("weight")

    if not recipe_id:
        return HttpResponse("Param recipe_id in not supplied!",
                            status=HTTPStatus.BAD_REQUEST)
    if not product_id:
        return HttpResponse("Param product_id in not supplied!",
                            status=HTTPStatus.BAD_REQUEST)
    if not weight:
        return HttpResponse("Param weight in not supplied!",
                            status=HTTPStatus.BAD_REQUEST)

    recipe = get_object_or_404(Recipe, id=recipe_id)
    product = get_object_or_404(Product, id=product_id)

    recipe_product, _ = RecipeProducts.objects.get_or_create(
        recipe=recipe,
        product=product,
    )
    recipe_product.weight = weight
    recipe_product.save()

    return HttpResponse(content="Successfully created", status=HTTPStatus.OK)


@require_http_methods(["GET"])
def cook_recipe(request):
    recipe_id = request.GET.get("recipe_id")
    if not recipe_id:
        return HttpResponse("Param recipe_id in not supplied!",
                            status=HTTPStatus.BAD_REQUEST)

    products = Product.objects.filter(
        recipeproducts__recipe_id=recipe_id
    ).all()
    for product in products:
        product.cooking_counter += 1
    Product.objects.bulk_update(products, fields=("cooking_counter",))

    return HttpResponse(
        content=f"Successfully cooked",
        status=HTTPStatus.OK
    )


@require_http_methods(["GET"])
def show_recipes_without_product(request):
    product_id = request.GET.get("product_id")
    if not product_id:
        return HttpResponse("Param product_id in not supplied!",
                            status=HTTPStatus.BAD_REQUEST)

    recipes = (Recipe.objects.exclude(products__id=product_id) |
               Recipe.objects.filter(
                   products__id=product_id,
                   recipeproducts__weight__lt=10
               ))

    return render(
        request,
        "recipe_table.html",
        {"recipes": recipes}
    )
