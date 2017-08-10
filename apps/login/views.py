from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Entity
  # the index function is called when root is visited

def index(request):

    # user just wants to load the page
    if request.method == 'GET':
        return render(request, 'login/index.html')

    # user is sending a post with credentials
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/success')
        else:
            return render(request, 'login/index.html', {'login_error': 'Invalid user or password'})

def logout_view(request):
    logout(request)

    return render(request, 'login/index.html')

def success(request):
    context = {
        'ents': Entity.objects.all()
    }
    return render(request, 'login/success.html', context)

def create(request):
    Entity.objects.create(entity_name=request.POST['entity_name'],state_of_inc=request.POST['state_of_inc'],date_of_inc=request.POST['date_of_inc'],)

    return redirect('/success')

def destroy(request, id):
    Entity.objects.get(id=id).delete()
    return redirect('/success')

def edit(request, id):
    context = {
        'ents': Entity.objects.get(id=id)
    }
    return render(request, 'login/update.html', context)

def update(request, id):

    #return redirect('entity/{}/edit'.format(id))

    ent_to_update = Entity.objects.get(id=id)
    ent_to_update.entity_name = request.POST['entity_name']
    ent_to_update.state_of_inc = request.POST['state_of_inc']
    ent_to_update.date_of_inc = request.POST['date_of_inc']
    ent_to_update.save()
    return redirect('/success')
