from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def analyze(request):
    context = {"code_result": "python"}
    word = {"code_result": request.POST["item_text"]}
    return render(request, 'index.html', word)
