from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mainapp/lobby.html')

def list1(request):
    return render(request, 'mainapp/list1.html')

def list2(request):
    return render(request, 'mainapp/list2.html')
