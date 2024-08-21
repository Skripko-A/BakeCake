from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def show_main(request):
    # TODO: Add db data
    context = {
        'levels': [{'id': 1, 'amount': 1, 'price': 400}, {'id': 2, 'amount': 2, 'price': 750}, {'id': 3, 'amount': 3, 'price': 1100}],
        'forms': [{'id': 1, 'title': 'Круг', 'price': 600}, {'id': 2, 'title': 'Квадрат', 'price': 400}, {'id': 3, 'title': 'Прямоугольник', 'price': 1000}],
        'toppings': [{'id': 1, 'title': 'Без', 'price': 0}, {'id': 2, 'title': 'Белый соус', 'price': 200}, {'id': 3, 'title': 'Карамельный', 'price': 180}, {'id': 4, 'title': 'Кленовый', 'price': 200}],
        'berries': [{'id': 1, 'title': 'Ежевика', 'price': 400}, {'id': 2, 'title': 'Малина', 'price': 300}, {'id': 3, 'title': 'Голубика', 'price': 450}],
        'decors': [{'id': 1, 'title': 'Фисташки', 'price': 300}, {'id': 2, 'title': 'Безе', 'price': 400}, {'id': 3, 'title': 'Фундук', 'price': 350}],
        'js_costs': {
            'Levels': [0, 400, 750, 1100],
            'Forms': [0, 600, 400, 1000],
            'Toppings': [0, 0, 200, 180, 200, 300, 350, 200],
            'Berries': [0, 400, 300, 450, 500],
            'Decors': [0, 300, 400, 350, 300, 200, 280],
            'Words': 500
        },
        'js_data': {
            'Levels': ['не выбрано', '1', '2', '3'],
            'Forms': ['не выбрано', 'Круг', 'Квадрат', 'Прямоугольник'],
            'Toppings': ['не выбрано', 'Без', 'Белый соус', 'Карамельный', 'Кленовый', 'Черничный', 'Молочный шоколад', 'Клубничный'],
            'Berries': ['нет', 'Ежевика', 'Малина', 'Голубика', 'Клубника'],
            'Decors': ['нет', 'Фисташки', 'Безе', 'Фундук', 'Пекан', 'Маршмеллоу', 'Марципан']
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
    context = {
        'cakes': [
            {
                'id': 1,
                'title': 'Торт 1',
                'image': 'img/image1.png'
            },
            {
                'id': 2,
                'title': 'Торт 2',
                'image': 'img/image2.png'
            },
            {
                'id': 3,
                'title': 'Торт 3',
                'image': 'img/image3.png'
            },
            {
                'id': 4,
                'title': 'Торт 4',
                'image': 'img/image2.png'
            },
            {
                'id': 5,
                'title': 'Торт 5',
                'image': 'img/image3.png'
            },
            {
                'id': 6,
                'title': 'Торт 6',
                'image': 'img/image1.png'
            },
        ]
    }
    return render(request, 'cakes_catalog.html', context)


def cake_page(request, cake_id: int):
    context = {
        'title': 'Торт 1',
        'image': '',
        'description': 'Описание',
        'levels_number': 1,
        'shape': 'круг',
        'topping': '',
        'berrie': '',
        'decor': '',
        'inscription': 'надпись'
    }
    return render(request, 'cake_page.html', context)
