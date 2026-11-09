
from django.shortcuts import render, redirect
from .models import Auto
from .forms import AutoForm


def agregar_auto(request):
    if request.method == 'POST':
        formulario = AutoForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('lista_autos')
    else:
        formulario = AutoForm()

    return render(request, 'autos/agregar_auto.html', {
        'formulario': formulario
    })


def lista_autos(request):
    autos = Auto.objects.all()

    return render(request, 'autos/lista_autos.html', {
        'autos': autos
    })
