from django.http import HttpResponse
from django.template import loader


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