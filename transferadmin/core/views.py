from django.shortcuts import render, redirect
from .models import Cliente, Transfer
from .forms import ClienteForm, TransferForm

# Create your views here.
def home(request):
    if request.method=='POST': 
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid:
            cliente_form.save()
            return redirect ('transfer')
    else:
        cliente_form =ClienteForm()
    return render(request, 'home.html', {'cliente_form': cliente_form})

def datos(request):
    clientes = Cliente.objects.all()
    transfers = Transfer.objects.all()
    datoss= {
        'clientes' : clientes,
        'transfers' : transfers
    }
    return render(request, 'datos.html', datoss)

def transfer(request):
    clientes = Cliente.objects.all()
    transfers = Transfer.objects.all()
    datoss= {
        'clientes' : clientes,
        'transfers' : transfers
    }
    return render(request, 'transfer.html', datoss)

def realizado(request):
    clientes = Cliente.objects.all()
    transfers = Transfer.objects.all()
    realizado= {
        'clientes' : clientes,
        'transfers' : transfers
    }
    return render(request, 'realizado.html', realizado)