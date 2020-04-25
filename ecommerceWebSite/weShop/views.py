from django.shortcuts import render



def index(request):
    context = {"weatherObject": "jsonResponse"}
    return render(request, 'index.html')