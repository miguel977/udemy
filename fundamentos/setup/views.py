from django.shortcuts import render

def homepage(request):
    nome = 'Fulano'
    pessoa = {
        'nome': 'Maria',
        'idade': 30,
        'cidade':'São Paulo'
    }
    return render(request, 'home.html')

def about(request):
    frutas = ['Maçã', 'Banana', 'Laranja', 'Uva']
    return render(request, 'about.html', {'frutas':frutas})