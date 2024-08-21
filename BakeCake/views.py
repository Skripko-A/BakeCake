from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def show_main(request):
    template = loader.get_template('index.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


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
        'description': 'Описание тортаsdaifda sgjklasdglk hgasdfhkjlag fsdkjh gfadshkljgaf iasih gih uraeihgu',
        'levels_number': 1,
        'shape': 'круг',
        'topping': '',
        'berrie': '',
        'decor': '',
        'inscription': 'надпись'
    }
    return render(request, 'cake_page.html', context)
