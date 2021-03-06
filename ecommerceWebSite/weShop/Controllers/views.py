from django.shortcuts import render, get_object_or_404 , redirect
from django.http import HttpResponse
from json import dumps
from django.contrib.auth.decorators import login_required
from validate_email import validate_email

from .AbstractController import parmsToMaps
from weShop.forms import orderForm
from weShop.Application.ContactApp import ContactApp
from weShop.Dto.ContactDto import ContactDto
from weShop.Models.models import Subscribe, Product, Category, Service, OrderItem, Order, Country
from django.conf import settings

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
        # TODO add validation more validation
        mostSalles = Product.objects.all().order_by('-rank')[:6]  # get last 6 items
        product = Product.objects.filter(id=slug)
        context["mostSalles"] = mostSalles
        context['products'] = product
        return render(request, 'shop-single.html', context=context)

    except Exception as e:
        print(e)
        return render(request, 'shop-single.html', context=context)

def cart(request):
    context = {}
    if request.user.is_authenticated:
        carts = OrderItem.objects.filter(user=request.user)
        context["carts"] = carts
        context["total"] = getTotal(carts)
    return render(request, 'cart.html', context=context)

@login_required()
def addOrUpdate(request):
    data = {}

    try:
        if request.method != "POST":
            data['response'] = 'Only POST request supported'
            data['status'] = 405
            return HttpResponse(dumps(data), content_type="application/json")

        slug = request.POST.get('slug')
        quantity = request.POST.get('quantity')

        if slug is None:
            data['response'] = 'all parms is required'
            data['status'] = 400
            return HttpResponse(dumps(data), content_type="application/json")

        checkQuantity = isInit(num=quantity)

        if not checkQuantity:
            data['response'] = 'negative number is not acceptable'
            data['status'] = 400
            return HttpResponse(dumps(data), content_type="application/json")


        item = get_object_or_404(Product, id=slug)

        oldOrders = OrderItem.objects.filter(user=request.user, product=item)

        if len(oldOrders) == 0:
            OrderItem.objects.get_or_create(product=item, user=request.user, quantity=quantity)
            data["response"] = "add to cart"
            data['status'] = 200
            data['incart'] = getItemIncart(request.user)
            request.session['card'] = getItemIncart(request.user) # update user session with the new number of items
            return HttpResponse(dumps(data), content_type="application/json")

        else:
            for oldOrder in oldOrders:
                if quantity is None:
                    oldOrder.quantity += 1
                else:
                    oldOrder.quantity += int(quantity)
                oldOrder.save()
                data["response"] = "Update cart"
                data['status'] = 200
                data['incart'] = getItemIncart(request.user)
                request.session['card'] = getItemIncart(request.user) # update user session with the new number of items
                return HttpResponse(dumps(data), content_type="application/json")

    except (KeyError, Product.DoesNotExist):
        data["response"] = "Something is wrong"
        data['status'] = 500
        return HttpResponse(dumps(data), content_type="application/json")

def getTotal(carts):
    total = 0
    for cart in carts:
        total += cart.get_total_item_price()
    return total

def getItemIncart(user):
    """
    this function used to caclcule number of itme in cart for the current user
    :param user: user who send the request
    :return: total items in cart
    """
    return len(OrderItem.objects.filter(user=user))

@login_required()
def deleteFromCart(request, slug):
    item = get_object_or_404(Product, id=slug)
    OrderItem.objects.filter(product=item).delete()
    request.session['card'] = getItemIncart(request.user)
    return redirect('cart')

@login_required()
def checkout(request):
    context = {}
    try:

        if request.method == 'GET':
            carts = OrderItem.objects.filter(user=request.user)
            countrys = Country.objects.all()

            context["countrys"] = countrys
            context["carts"] = carts
            context["total"] = getTotal(carts)
            form = orderForm()
            context['form'] = form
            return render(request, 'checkout.html', context=context, )

        elif request.method == 'POST':

            data = request.POST
            form = orderForm(data=data)

            if form.is_valid():
                form.save()


                return redirect('thankyou')


            carts = OrderItem.objects.filter(user=request.user)
            countrys = Country.objects.all()

            context["countrys"] = countrys
            context["carts"] = carts
            context["total"] = getTotal(carts)
            context['errors'] = form.errors
            return render(request, 'checkout.html', context=context)

        else:
            pass

    except Exception as e:
        print(e)

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
        return HttpResponse(dumps(data), content_type="application/json")

################### Page Contact ####################################
def contact(request):
    data = {}
    try:
        if request.method == 'GET':
            return render(request, 'contact.html')

        elif request.method == 'POST':
            postParams = ['firstname', 'lastname', 'email', 'subject', 'message'] # expected params
            params = parmsToMaps(request, postParams) # extrcat params form request
            contactDto = ContactDto(params=params) # input dto
            outputDto = ContactApp.add(contactDto) # la couche app
            data['data'] = outputDto # output dto

            return HttpResponse(dumps(data), content_type="application/json")

        else:
            data['error'] = 'Only POST, GET request supported'
            data['statusCode']
            context = {"data": data}
            return render(request, 'contact.html', context=context)

    except Exception as e:
        raise Exception(e)
        data['error'] = "something wrrong please try later !!!"
        return HttpResponse(dumps(data), content_type="application/json")



################### class Utils ######################################
def isInit\
                (num):
    try:
        num = int(num)
        if isinstance(num, int):
            if int(num) > 0:
                return True
        return False
    except ValueError:
        return False
