from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def suma(request,op1,op2):
    return HttpResponse("<h1>Suma!</h1><p>" + op1 + " + " + op2 + " = " + str(int(op1) + int(op2)) + "</p>")

def resta(request,op1,op2):
    return HttpResponse("<h1>Resta!</h1><p>" + op1 + " - " + op2 + " = " + str(int(op1) - int(op2)) + "</p>")

def mult(request,op1,op2):
    return HttpResponse("<h1>Multiplicacion!</h1><p>" + op1 + " * " + op2 + " = " + str(int(op1) * int(op2)) + "</p>")

def div(request,op1,op2):
    return HttpResponse("<h1>Division!</h1><p>" + op1 + " / " + op2 + " = " + str(float(op1) / float(op2)) + "</p>")

def notFound(request):
    return HttpResponse("<h1>Error</h1><p>Please enter a valid operation.</p>", status=400)
