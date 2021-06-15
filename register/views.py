from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate


# Create your views here.
def register(request):
    if 'POST' == request.method:
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
    
    else:
        form = UserCreationForm()
    
    context = {
        'form' : form
    }

    return render(request, 'register/UserCreation.html', context)