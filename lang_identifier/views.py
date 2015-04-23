from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if request.method == 'POST':
        code_reuslt = "python"
        return redirect('/', {'code_result': code_result})
    return render(request, 'index.html')
