from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .predict_language import make_prediction_from_text
from .models import CodeSnippet

# Create your views here.
def index(request):
    return render(request, 'index.html')

def analyze(request):
    text = request.POST['item_text']
    predictions = make_prediction_from_text(text)
    context = {"code_result": predictions}
    word = {"code_result": request.POST["item_text"]}
    CodeSnippet.objects.create(code=text,answer=predictions[0][0])
    return render(request, 'index.html', context)

def confim(request):
    confrimation = request.POST['confirmation']
    code_snippit = request.POST['code_snippet']
    if confrimation == 'Yes':
