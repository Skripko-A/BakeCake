from datetime import date, timedelta, datetime
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db import transaction
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from accounts.models import Client

from .models import Cake, Topping, Decor, Berry, Layer, Shape, Order
from .forms import OrderRegularCakeForm


def show_main(request):
    toppings = Topping.objects.order_by('pk')
    berries = Berry.objects.order_by('pk')
    decors = Decor.objects.order_by('pk')
    levels = Layer.objects.order_by('pk')
    forms = Shape.objects.order_by('pk')

    context = {
        'levels': levels,
        'forms': forms,
        'toppings': toppings,
        'berries': berries,
        'decors': decors,
        'js_costs': serialize_js_costs(
            toppings, berries, decors, levels, forms
        ),
        'js_data': serialize_js_data(
            toppings, berries, decors, levels, forms
        )
    }

    return render(request, 'index.html', context)


def serialize_js_data(toppings, berries, decors, levels, forms):
    not_chosen = ['не выбрано']
    not_present = ['нет']

    levels = not_chosen + [level.number for level in levels]
    forms = not_chosen + [shape.get_title_display() for shape in forms]
    toppings = not_chosen + [topping.title for topping in toppings]
    berries = not_present + [berry.title for berry in berries]
    decors = not_present + [decor.title for decor in decors]

    return {
        'Levels': levels,
        'Forms': forms,
        'Toppings': toppings,
        'Berries': berries,
        'Decors': decors
    }


def serialize_js_costs(toppings, berries, decors, levels, forms):
    free = 0

    levels = [free] + [int(level.price) for level in levels]
    forms = [free] + [int(shape.price) for shape in forms]
    toppings = [free] + [int(topping.price) for topping in toppings]
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


def show_lk(request, client_id: int):
    requested_client = Client.objects.get(id=client_id)
    return render(request, 'lk.html', {"user": requested_client})


def show_lk_order(request):
    template = loader.get_template('lk-order.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


def cakes_catalog(request):
    context = {'cakes': Cake.objects.all()}
    return render(request, 'cakes_catalog.html', context)


def cake_page(request, cake_id: int, errors=None):
    requested_cake = Cake.objects\
        .select_related('topping', 'berry', 'decor', 'shape', 'levels_number')\
        .get(id=cake_id)

    if request.user.is_authenticated:
        user = request.user
    else:
        user = None

    context = {
        'cake_id': cake_id,
        'title': requested_cake.title,
        'image': requested_cake.image.url,
        'description': requested_cake.description,
        'levels_number': requested_cake.levels_number.number,
        'shape': requested_cake.shape.get_title_display,
        'topping': requested_cake.topping.title,
        'berry': requested_cake.berry.title,
        'decor': requested_cake.decor.title,
        'inscription': requested_cake.inscription,
        'price': requested_cake.price,
        'user': user,
        'errors': errors
    }

    return render(request, 'cake_page.html', context)


@transaction.atomic()
def create_regular_cake_order(request, cake_id: int):
    if request.method == 'POST':
        form = OrderRegularCakeForm(request.POST)
        if not form.is_valid():
            return cake_page(request, cake_id, form.errors)
        order_data = form.cleaned_data

        name = order_data['name']
        email = order_data['email']
        phone_number = order_data['phone']
        address = order_data['address']

        user = get_ordering_user(request, name, email, phone_number, address)

        if not user.address:
            User = get_user_model()
            User.objects.filter(pk=user.id).update(address=address)

        comment = order_data['comment']
        delivery_comment = order_data['delivery_comment']
        delivery_date = order_data['date']
        delivery_time = order_data['time']

        cake = Cake.objects\
            .select_related('levels_number',
                            'topping',
                            'shape',
                            'berry',
                            'decor')\
            .get(pk=cake_id)

        total_price = cake.price
        plus_20 = None
        days_before_delivery = delivery_date - date.today()

        if not days_before_delivery >= timedelta(hours=24):
            plus_20 = total_price * Decimal(0.2)
            total_price += plus_20

        order = Order.objects.create(
            customer=user,
            name=name,
            email=email,
            phone=phone_number,
            address=address,
            date=delivery_date,
            time=delivery_time,
            comment=comment,
            delivery_comment=delivery_comment,
            price=total_price,
            cake=cake,
        )

        context = {
            'order': order,
            'plus_20': plus_20
        }

        return render(request, 'order_success.html', context)


def get_ordering_user(request, name, email, phone_number, address):
    if request.user.is_authenticated:
        user = request.user
    else:
        User = get_user_model()
        if User.objects.filter(phone_number=phone_number):
            user = User.objects.get(phone_number=phone_number)
        elif User.objects.filter(email=email):
            user = User.objects.get(email=email)
        else:
            user = User.objects.create_user(
                phone_number=phone_number,
                email=email,
                first_name=name,
                address=address
            )

    return user


@transaction.atomic()
def create_custom_cake_order(request):
    if request.method == 'POST':
        name = request.POST.get('NAME')
        email = request.POST.get('EMAIL')
        phone_number = request.POST.get('PHONE')
        address = request.POST.get('ADDRESS')

        user = get_ordering_user(request, name, email, phone_number, address)

        if not user.address:
            User = get_user_model()
            User.objects.filter(pk=user.id).update(address=address)

        # TODO: count order sum at Order model method when creating

        total_price = 0

        levels_number = Layer.objects.get(pk=request.POST.get('LEVELS')[0])
        total_price += levels_number.price

        shape = Shape.objects.get(pk=request.POST.get('FORM')[0])
        total_price += shape.price

        topping = Topping.objects.get(pk=request.POST.get('TOPPING')[0])
        total_price += topping.price

        berry_id = request.POST.get('BERRIES')
        berry = Berry.objects.get(pk=berry_id[0]) if berry_id else None
        if berry:
            total_price += berry.price

        decor_id = request.POST.get('DECOR')
        decor = Decor.objects.get(pk=decor_id[0]) if decor_id else None
        if decor:
            total_price += decor.price

        inscription = request.POST.get('WORDS')
        if not inscription:
            inscription = None
        else:
            total_price += 500

        comment = request.POST.get('COMMENTS')
        delivery_comment = request.POST.get('DELIVCOMMENTS')
        delivery_date = request.POST.get('DATE')
        delivery_time = request.POST.get('TIME')

        plus_20 = None
        days_before_delivery = datetime.strptime(
            delivery_date, '%Y-%m-%d'
        ).date() - date.today()

        if not days_before_delivery >= timedelta(hours=24):
            plus_20 = total_price * Decimal(0.2)
            total_price += plus_20

        order = Order.objects.create(
            customer=user,
            name=name,
            email=email,
            phone=phone_number,
            address=address,
            date=delivery_date,
            time=delivery_time,
            comment=comment,
            delivery_comment=delivery_comment,
            levels_number=levels_number,
            shape=shape,
            topping=topping,
            berry=berry,
            decor=decor,
            inscription=inscription,
            price=total_price
        )

        context = {
            'order': order,
            'plus_20': plus_20
        }

        return render(request, 'order_success.html', context)
