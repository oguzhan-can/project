from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'login.html')

def montaj(request):
    return render(request, 'montaj.html')

def uretim(request):
    return render(request, 'uretim.html')

def anasayfa(request):
    return render(request, 'anasayfa.html')

def personel(request):
    return render(request, 'personel.html')
