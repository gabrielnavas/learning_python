from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.template import loader

from .models import Produto

def index(request):

    produtos = Produto.objects.all()
    # print(produtos)

    context = {
        'curso': 'aprendendo django na udemy',
        'nhé': 'Yahoooowwwwwwwwww',
        'produtos': produtos,
    }

    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, id):
    # prod = Produto.objects.get(id=id)
    prod = get_object_or_404(Produto, id=id) #mais seguro

    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html', charset='utf-8', status=404)

def error500(request):
    template = load.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html', charset='utf-8', status=500)
