# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response

from models import ItemAgenda

def lista(request):
    lista_itens = ItemAgenda.objects.all()
    return render_to_response("lista.html", {'lista_itens': lista_itens})

