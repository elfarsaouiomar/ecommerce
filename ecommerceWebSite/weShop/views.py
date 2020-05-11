from django.shortcuts import render
from django.http import HttpResponse
from json import dumps
from validate_email import validate_email

from app.ContactApp import ContactApp
from dto.ContactDto import ContactDto
from .models import Subscribe, Product, Category, Service




def parmsToMaps(req, args):
    """
    :param req: reuqest type post, GET
    :param args: list of params
    :return: dict contain params and value
    """
    params = {}
    for param in args:
        if req.method == "POST":
            value = req.POST.get(param)
            params[param] = value

        elif req.method == "GET":
            value = req.GET.get(param)
            if value is not None:
                params[param] = value
    return params

def index(request):
    context = {}
    catigorys = Category.objects.all()
    services = Service.objects.all()
    mostSalles = Product.objects.all().order_by('-rank')[:6]

    context["mostSalles"] = mostSalles
    context["catigorys"] = catigorys
    context["services"] = services
    return render(request, 'index.html', context=context)


def Search(request):
    pass

def shop(request):
    context = {}
    products = Product.objects.all().order_by('-dateDeCreation')
    catigorys = Category.objects.all()
    context["products"] = products
    context["catigorys"] = catigorys
    return render(request, 'shop.html', context=context)

def categorys(request, slug):
    try:
        if request.method == "GET":
            if slug:
                catigorys = Product.objects.filter(category_id=slug)
            else:
                catigorys = Product.objects.all()

            context = {"products": catigorys}
            return render(request, 'shop.html', context=context)
        else:
            return redirect(request, 'index')

    except Exception as err:
        print (err)

def singleProduct(request, slug):
    context = {}
    try:
        if request.method == "GET":
            if slug:
                product = Product.objects.filter(id=slug)
                context['products'] = product
                return render(request, 'shop-single.html', context=context)
    except Exception as e:
        print (e)

def cart(request):
    return render(request, 'cart.html')

def addTocart(request):
    pass

def deleteFromCart(request):
    pass

def checkout(request):
    return render(request, 'checkout.html')

def thankyou(request):
    return render(request, 'thankyou.html')

def subscribe(request):
    data = {}
    try:
        if request.method != "POST":
            data['response'] = 'Only POST request supported'

        email = request.POST.get('email')
        if email is None:
            data['response'] = 'email is required'

        is_valid = validate_email(email)
        if is_valid:
            subscribe = Subscribe()
            subscribe.email = email
            subscribe.save()
            data['response'] = 'thank you for subscribe'
        else:
            data['response'] = 'email is invalid'

    except Exception as e:
        print(e)
        data['response'] = "somethings wrrong !"

    finally:
        return HttpResponse(dumps(data), content_type="application/json")


################### Page Contact ####################################
def contact(request):
    data = {}
    context = {}
    try:
        if request.method == 'GET':
            return render(request, 'contact.html')

        elif request.method == 'POST':
            postParams = ['fname', 'lname', 'email', 'subject', 'message']
            params = parmsToMaps(request, postParams)
            contactDto = ContactDto(params=params)
            contactDto.validate()

            # check if dto return error
            if len(contactDto.errors) != 0:
                context["data"] = contactDto.errors
                context['postParams'] = params
                return render(request, 'contact.html', context=context)
            else:
                contactApp = ContactApp()
                contactApp.add(contactDto.data)
                data['response'] = "thank you for your message"
                context = {"data": data}
                return render(request, 'contact.html', context=context)
        else:
            data['error'] = 'Only POST, GET request supported'
            context = {"data": data}
            return render(request, 'contact.html', context=context)

    except Exception as e:
        print(e)
        data['error'] = "something wrrong please try later !!!"
        context = {"data": data}
        return render(request, 'contact.html', context=context)
