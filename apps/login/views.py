from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib.messages import error
  # the index function is called when root is visited

def index(request):
    return render(request, 'login/index.html')

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('login/success.html')
    else:
        if len(errors):
            for field, message in errors.items():
                error(request, message, extra_tags=field)

        return redirect('login/index.html')

    return render(request, 'login/success.html')
