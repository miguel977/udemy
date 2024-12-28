from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def desafio_semana(request, dia):
    desafio = ''
    if dia == 'domingo':
        desafio = 'Ler Livro sobre Django'
    elif dia == 'segunda':
        desafio = 'Assistir Série Breaking Bad'
    elif dia == 'terça':
        desafio = 'Estudar programação Python'
    else:
        return HttpResponseNotFound("Não há desafio para este dia informado")
    return HttpResponse(desafio)




