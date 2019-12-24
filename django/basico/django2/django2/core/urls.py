from django.urls import path

from core.views import index, contato, produto

urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('produto/<int:id>', produto, name='produto_nome_exemplo'),
]