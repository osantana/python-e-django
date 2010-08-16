# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response

from models import ItemAgenda
from forms import FormItemAgenda

def lista(request):
    lista_itens = ItemAgenda.objects.all()
    return render_to_response("lista.html", {'lista_itens': lista_itens})

def adiciona(request):
    if request.method == 'POST': # Formulário enviado
        form = FormItemAgenda(request.POST, request.FILES)
        if form.is_valid():
            # Formulário válido.
            dados = form.cleaned_data
            item = ItemAgenda(data=dados['data'], hora=dados['hora'],
                              titulo=dados['titulo'], descricao=dados['descricao'])
            item.save()

            # Mensagem de formulário cadastrado
            return render_to_response("salvo.html", {})
    else:
        # Exibe formulário em branco
        form = FormItemAgenda()

    return render_to_response("adiciona.html", {'form': form})

