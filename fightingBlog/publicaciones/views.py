from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse

 
def Inicio(request):
    template_name= 'index.html'
    ctx={
        
    }
    return render(request, template_name, ctx)