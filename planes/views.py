from django.http import request
from django.http.request import HttpRequest
from django.shortcuts import redirect, render, get_object_or_404
from .models import Plan, Plan_Contratado
from django.utils import timezone
from .forms import PlanForm

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