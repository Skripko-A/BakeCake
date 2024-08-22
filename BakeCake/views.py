from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Cake, Topping, Decor, Berry


def show_main(request):
    all_toppings = Topping.objects.order_by('pk')
    no_topping = all_toppings.get(title='Без топпинга')
    toppings_with_price = all_toppings.exclude(id=no_topping.id)
    toppings_for_index_page = [no_topping] + list(toppings_with_price)

    berries = Berry.objects.order_by('pk')
    decors = Decor.objects.order_by('pk')
    forms = [{'id': shape_id, 'title': shape}
             for shape_id, shape in enumerate(Cake.shapes.values(), 1)]

    context = {
        'levels': [
            {'id': 1, 'amount': 1},
            {'id': 2, 'amount': 2},
            {'id': 3, 'amount': 3}
        ],
        'forms': forms,
        'toppings': toppings_for_index_page,
        'berries': berries,
        'decors': decors,
        'js_costs': serialize_js_costs(
            no_topping, toppings_with_price, berries, decors
        ),
        'js_data': serialize_js_data(
            no_topping, toppings_with_price, berries, decors
        )
    }

    return render(request, 'index.html', context)


def serialize_js_data(no_topping, toppings_with_price, berries, decors):
    not_chosen = ['не выбрано']
    not_present = ['нет']

    levels = not_chosen + ['1', '2', '3']
    forms = not_chosen + [shape for shape in Cake.shapes.values()]
    toppings = not_chosen + [no_topping.title] + [
        topping.title for topping in toppings_with_price
    ]
    berries = not_present + [berry.title for berry in berries]
    decors = not_present + [decor.title for decor in decors]

    return {
        'Levels': levels,
        'Forms': forms,
        'Toppings': toppings,
        'Berries': berries,
        'Decors': decors
    }


def serialize_js_costs(no_topping, toppings_with_price, berries, decors):
    free = 0

    levels = [free] + [400, 750, 1100]
    forms = [free] + [600, 400, 1000]
    toppings = [free] + [int(no_topping.price)] \
        + [int(topping.price) for topping in toppings_with_price]
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
        .select_related('topping', 'berry', 'decor')\
        .get(id=cake_id)

    context = {
        'title': requested_cake.title,
        'image': requested_cake.image.url,
        'description': requested_cake.description,
        'levels_number': requested_cake.levels_number,
        'shape': requested_cake.get_shape_display,
        'topping': requested_cake.topping.title,
        'berry': requested_cake.berry.title,
        'decor': requested_cake.decor.title,
        'inscription': requested_cake.inscription
    }

    return render(request, 'cake_page.html', context)
