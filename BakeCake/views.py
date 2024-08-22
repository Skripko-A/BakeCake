from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Cake, Topping, Decor, Berry

def show_main(request):
    # TODO: Add db data
    context = {
        'levels': [{'id': 1, 'amount': 1, 'price': 400}, {'id': 2, 'amount': 2, 'price': 750}, {'id': 3, 'amount': 3, 'price': 1100}],
        'forms': [{'id': 1, 'title': 'Круг', 'price': 600}, {'id': 2, 'title': 'Квадрат', 'price': 400}, {'id': 3, 'title': 'Прямоугольник', 'price': 1000}],
        'toppings': Topping.objects.all(),
        'berries': Berry.objects.all(),
        'decors': Decor.objects.all(),
        'js_costs': {
            'Levels': [0, 400, 750, 1100],
            'Forms': [0, 600, 400, 1000],
            'Toppings': [topping.price for topping in Topping.objects.all()],
            'Berries': [berry.price for berry in Berry.objects.all()],
            'Decors': [decor.price for decor in Decor.objects.all()],
            'Words': 500
        },
        'js_data': {
            'Levels': ['не выбрано', '1', '2', '3'],
            'Forms': ['не выбрано', 'Круг', 'Квадрат', 'Прямоугольник'],
            'Toppings': [topping.title for topping in Topping.objects.all()],
            'Berries': [berry.title for berry in Berry.objects.all()],
            'Decors': [decor.title for decor in Decor.objects.all()]
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
        'shape': requested_cake.get_shape_display,
        'topping': requested_cake.topping.title,
        'berry': requested_cake.berry.title,
        'decor': requested_cake.decor.title,
        'inscription': requested_cake.inscription
    }
    return render(request, 'cake_page.html', context)
