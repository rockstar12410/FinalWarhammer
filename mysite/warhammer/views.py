from django.shortcuts import render, redirect
from .forms import usedForm

# Create your views here.
def index(request):
    return render(request, 'warhammer/Index.html')

def newbuy(request):
    return render(request, 'warhammer/new.html')

def usedbuy(request):
    return render(request, 'warhammer/used.html')

def usedform(request):
    form = usedForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'warhammer/form.html', {'form': form})

def checkout(request):
    return render(request, 'warhammer/checkout.html')