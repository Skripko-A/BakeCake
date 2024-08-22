from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Cake, Topping, Decor, Berry, Layer, Shape


def show_main(request):
    all_toppings = Topping.objects.order_by('pk')
    no_topping = all_toppings.get(title='Без топпинга')
    toppings_with_price = all_toppings.exclude(id=no_topping.id)
    toppings_for_index_page = [no_topping] + list(toppings_with_price)
    serialized_toppings = [{
        'id': topping_id,
        'title': topping.title,
        'price': topping.price
    } for topping_id, topping in enumerate(toppings_for_index_page, 1)]

    berries = Berry.objects.order_by('pk')
    decors = Decor.objects.order_by('pk')
    levels = Layer.objects.order_by('pk')
    forms = Shape.objects.order_by('pk')

    context = {
        'levels': levels,
        'forms': forms,
        'toppings': serialized_toppings,
        'berries': berries,
        'decors': decors,
        'js_costs': serialize_js_costs(
            no_topping, serialized_toppings, berries, decors, levels, forms
        ),
        'js_data': serialize_js_data(
            no_topping, serialized_toppings, berries, decors, levels, forms
        )
    }
    print(context)

    return render(request, 'index.html', context)


def serialize_js_data(no_topping, serialized_toppings, berries, decors, levels, forms):
    not_chosen = ['не выбрано']
    not_present = ['нет']

    levels = not_chosen + [level.number for level in levels]
    forms = not_chosen + [shape.get_title_display() for shape in forms]
    toppings = not_chosen + [topping['title'] for topping in serialized_toppings]
    berries = not_present + [berry.title for berry in berries]
    decors = not_present + [decor.title for decor in decors]

    return {
        'Levels': levels,
        'Forms': forms,
        'Toppings': toppings,
        'Berries': berries,
        'Decors': decors
    }


def serialize_js_costs(no_topping, serialized_toppings, berries, decors, levels, forms):
    free = 0

    levels = [free] + [int(level.price) for level in levels]
    forms = [free] + [int(shape.price) for shape in forms]
    toppings = [free] + [int(topping['price']) for topping in serialized_toppings]
    berries = [free] + [int(berry.price) for berry in berries]
    decors = [free] + [int(decor.price) for decor in decors]
    return {
        'Levels': levels,
        'Forms': forms,
        'Toppings': toppings,
        'Berries': berries,
        'Decors': decors,
        'Words': 500
    }


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
    requested_cake = Cake.objects\
        .select_related('topping', 'berry', 'decor', 'shape', 'levels_number')\
        .get(id=cake_id)

    context = {
        'title': requested_cake.title,
        'image': requested_cake.image.url,
        'description': requested_cake.description,
        'levels_number': requested_cake.levels_number.number,
        'shape': requested_cake.shape.get_title_display,
        'topping': requested_cake.topping.title,
        'berry': requested_cake.berry.title,
        'decor': requested_cake.decor.title,
        'inscription': requested_cake.inscription
    }

    return render(request, 'cake_page.html', context)
