from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Cake, Topping, Decor, Berry, Layer, Shape

def show_main(request):
    layers = Layer.objects.all(),
    shapes = Shape.objects.all(),
    toppings = Topping.objects.all(),
    berries = Berry.objects.all(),
    decors = Decor.objects.all(),
    # TODO: Add db data
    context = {
        'levels': layers,
        'forms': shapes,
        'toppings': toppings,
        'berries': berries,
        'decors': decors,
        'js_costs': {
            'Levels': [layer.price for layer in layers],
            'Forms': [shape.price for shape in shapes],
            'Toppings': [topping.price for topping in toppings],
            'Berries': [berry.price for berry in berries],
            'Decors': [decor.price for decor in decors],
            'Words': 500
        },
        'js_data': {
            'Levels': [layer.number for layer in layers],
            'Forms': [shape.title for shape in shapes],
            'Toppings': [topping.title for topping in toppings],
            'Berries': [berry.title for berry in berries],
            'Decors': [decor.title for decor in decors]
        }
    }
    return render(request, 'index.html', context)


def show_lk(request):
    template = loader.get_template('lk.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


def show_lk_order(request):
    template = loader.get_template('lk-order.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


def cakes_catalog(request):
    context = {'cakes': Cake.objects.all()}
    return render(request, 'cakes_catalog.html', context)


def cake_page(request, cake_id: int):
    requested_cake = Cake.objects.get(id=cake_id)
    context = {
        'title': requested_cake.title,
        'image': requested_cake.image.url,
        'description': requested_cake.description,
        'levels_number': requested_cake.levels_number,
        'shape': requested_cake.shape.get_title_display,
        'topping': requested_cake.topping.title,
        'berry': requested_cake.berry.title,
        'decor': requested_cake.decor.title,
        'inscription': requested_cake.inscription
    }
    return render(request, 'cake_page.html', context)
