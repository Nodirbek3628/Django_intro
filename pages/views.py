from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_wr (x):
    return HttpResponse('salom home ')

def a_wr (a):
    return HttpResponse('salom about')

def c_wr (a):
    return HttpResponse('salom contact')

def l_wr (a):
    return HttpResponse('salom login')

def p_wr (a):
    return HttpResponse('salom profile')

def r_wr (a):
    return HttpResponse('<h1> salom registr <h1/>')

