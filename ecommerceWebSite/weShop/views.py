from django.shortcuts import render, get_object_or_404 , redirect
from django.http import HttpResponse
from json import dumps
from django.contrib.auth.decorators import login_required
from validate_email import validate_email

from .app.ContactApp import ContactApp
from .dto.ContactDto import ContactDto
from .models import Subscribe, Product, Category, Service, OrderItem, Order



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
    catigorys = Category.objects.all() # get all categorys
    services = Service.objects.all() # get all services
    mostSalles = Product.objects.all().order_by('-rank')[:6] # get last 6 items

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
    context = {}
    if request.user.is_authenticated:
        carts = OrderItem.objects.filter(user=request.user)
        context["carts"] = carts
    return render(request, 'cart.html', context=context)

@login_required()
def addTocart(request, slug):
    data = {}
    try:
        item = get_object_or_404(Product, id=slug)

        oldOrders = OrderItem.objects.filter(user=request.user, product=item)

        if len(oldOrders) == 0:
            OrderItem.objects.get_or_create(product=item, user=request.user)
            data["cart"] = "add to cart"
            return redirect('cart')

        else:
            for oldOrder in oldOrders:
                oldOrder.quantity += 1
                oldOrder.save()
            return redirect('cart')

    except (KeyError, Product.DoesNotExist):
        return redirect('shop')

def getItemIncart(user):
    return len(OrderItem.objects.filter(user=user))

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
            return HttpResponse(dumps(data), content_type="application/json")

        email = request.POST.get('email')
        if len(email) == 0:
            data['response'] = 'email is required'
            return HttpResponse(dumps(data), content_type="application/json")

        is_valid = validate_email(email)
        if is_valid:
            subscribe = Subscribe()
            subscribe.email = email
            subscribe.save()
            data['response'] = 'Thank you for subscribe'
            return HttpResponse(dumps(data), content_type="application/json")
        else:
            data['response'] = 'Email is invalid'
            return HttpResponse(dumps(data), content_type="application/json")

    except Exception as e:
        print(e)
        data['response'] = "somethings wrrong !"

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
