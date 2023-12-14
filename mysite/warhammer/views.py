from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
import pdfkit
from .forms import usedForm
from .models import NewBuy
from .models import checkout
from .models import usedBuy
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request, 'warhammer/Index.html')

def newbuy(request):
    newlist = NewBuy.objects.all()
    prod_name = request.GET.get('name')
    if prod_name != '' and prod_name is not None:
        newlist = NewBuy.objects.filter(product__contains=prod_name)
    prod_tag = request.GET.get('tag')
    if prod_tag != '' and prod_tag is not None:
        newlist = NewBuy.objects.filter(tags__contains=prod_tag)
    additem = request.POST.get("ID")
    if additem != None:
        newitem = NewBuy.objects.get(id = additem)
        nprices = newitem.price
        nproducts = newitem.product

        ncheckouts = checkout.objects.create(product= nproducts, price= nprices, type='new')

    paginator = Paginator(newlist, 5)
    page = request.GET.get('page')
    newlist = paginator.get_page(page)




    return render(request, 'warhammer/new.html', {'newlist': newlist})

def usedbuy(request):
    usedlist = usedBuy.objects.all()
    prod_name = request.GET.get('name')
    if prod_name != '' and prod_name is not None:
        usedlist = usedBuy.objects.filter(product__contains = prod_name)
    prod_tag = request.GET.get('tag')
    if prod_tag != '' and prod_tag is not None:
        usedlist = usedBuy.objects.filter(condition__contains = prod_tag)
    adduitem = request.POST.get("ID")
    if adduitem != None:
        useditem = usedBuy.objects.get(id = adduitem)
        uprices = useditem.price
        uproducts = useditem.product
        ucheckouts = checkout.objects.create(product = uproducts, price = uprices, type='used')

    paginator = Paginator(usedlist, 5)
    page = request.GET.get('page')
    usedlist = paginator.get_page(page)

    return render(request, 'warhammer/used.html', {'usedlist':usedlist})

def usedform(request):
    form = usedForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'warhammer/form.html', {'form': form})

def atcheckouts(request):
    finals = checkout.objects.all()
    totalcost = 0
    for item in finals:
        totalcost += item.price

    context = {
        'final': finals,
        'totalcost': totalcost
    }

    return render(request, 'warhammer/checkout.html', context)

def checkreciept(request):
    finals = checkout.objects.all()
    totalcost = 0
    for item in finals:
        totalcost += item.price

    context = {
        'final': finals,
        'totalcost': totalcost
    }
    template = loader.get_template('warhammer/checkreciept.html')
    html = template.render(context)
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8'
    }
    # ran into a error that it wasn't heading to the executable, so i had to add the line below to make it work.
    # and add a config to the pdf variable.
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    pdf = pdfkit.from_string(html, False, options, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = "reciept.pdf"
    checkout.objects.all().delete()
    return response