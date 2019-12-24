from django.shortcuts import render
from .models import Produto

def index(request):
    print(request)
    print(dir(request))
    print(f'Método: {request.method}')
    print(f'Cabeçalhos: {request.headers}')
    print(f"User-Agent: {request.headers['User-Agent']}")
    print(f"User: {request.user}")
    print(f'User Data: {dir(request.user)}')

    logado = str(request.user)
    print(logado)

    prod_query_list = Produto.objects.all()

    context = {
        "texto_pagina": "Olá jovem meu nome é josevaldosky e moro aqui no Prucia!!",
        'outro_texto': "IAAAAAAAAAAruuu!! ;)",
        'logado': 'logado' if logado is not 'AnonymousUser' else f'não logado: {logado}',
        'produtos': prod_query_list,
    }
    return render(request, 'index.images', context)


def contact(request):
    return render(request, 'contact.images')

def produto(request, id):
    print(f'PK: {id}')
    prod = Produto.objects.get(id=id)

    context = {
        'produto': prod
    }
    return render(request, 'produto.images', context)