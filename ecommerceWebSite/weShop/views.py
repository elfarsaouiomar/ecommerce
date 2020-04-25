from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from json import dumps
from validate_email import validate_email
from .models import Subscribe


def index(request):
    return render(request, 'index.html')

def shop(request):
    return render(request, 'shop.html')

def singleProduct(request):
    return render(request, 'shop-single.html')

def contact(request):
    return render(request, 'contact.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def thankyou(request):
    return render(request, 'thankyou.html')

def subscribe(request):
    data = {}

    try:
        if request.method == "POST":  # os request.GET()
            email = request.POST.get('email')
            if email is not None:
                is_valid = validate_email(email)
                if is_valid:
                    subscribe = Subscribe()
                    subscribe.email = email
                    subscribe.save()
                    data['response'] = 'thank you for subscribe'
                else:
                    data['response'] = 'email is invalid'
            else:
                data['response'] = 'email is required'
        else:
            data['response'] = 'Only POST request supported'

    except Exception as e:
        print(e)
        data['response'] = "somethings wrrong !"

    finally:
        return HttpResponse(dumps(data), content_type="application/json")

