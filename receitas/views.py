from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'receitas/paginas/home.html')


def receitas(request, id):
    return render(request, 'receitas/paginas/view-receitas.html')
