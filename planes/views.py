from django.http import request
from django.http.request import HttpRequest
from django.shortcuts import redirect, render, get_object_or_404
from .models import Plan, Plan_Contratado
from django.utils import timezone


from .models import *
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm
from django.contrib.auth import login, authenticate

# Create your views here.

def plan_list(request):
    planes = Plan.objects.all()
    return render(request, 'planes/plan_list.html', {'planes': planes})

def plan_venta(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    return render(request, 'planes/plan_venta.html', {'plan' : plan}) 




def plan_contrato(request, pk):
    Plan_Contratado.idUser = request.user
    Plan_Contratado.idPlan = get_object_or_404(Plan, pk=pk) 
    Plan_Contratado.fechaPlan =  timezone.now()
    
    Plan_Contratado.save()
    return render(request, 'planes/plan_list.html', {})


def index2(request):
    return render(request, 'index2.html')

def login(request):
    return render(request, 'login.html')

def registrar(request):
    data= {
        'form':CustomUserForm()
    }

    if request.method == 'POST': 
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #autenticar al usuario y rediridirlo al inicio
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            #login(request, user)
            return redirect(to='index2')
    
    return render(request, 'registration/registrar.html', data)

def logout(request):
    return render(request, 'logout')

def reset(request):
    return render(request, 'password_reset.html')

def contacto(request):
    return render(request, 'contacto.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def Mapa(request):
    return render(request, 'Mapa.html')