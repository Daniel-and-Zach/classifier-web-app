from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .predict_language import make_prediction_from_text

# Create your views here.
def index(request):
    return render(request, 'index.html')

def analyze(request):
    text = request.POST['item_text']
    context = {"code_result": make_prediction_from_text(text)}
    word = {"code_result": request.POST["item_text"]}
    return render(request, 'index.html', context)
