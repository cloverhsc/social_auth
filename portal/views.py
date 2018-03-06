# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.


# login
def userlogin(request):
    return render(request, 'login.html', locals())


# logout
def userlogout(request):
    result = {'code': 200, 'result': 'success', 'message': 'Success'}
    logout(request)
    return JsonResponse(result)


# home
def MyHome(request):
    return render(request, 'home.html')
