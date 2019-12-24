from django.urls import path

from .views import index, contact, produto

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contato'),
    path('produto/<int:id>', produto, name='produto'),
]