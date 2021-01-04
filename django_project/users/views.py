from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
    # form = UserCreationForm()
    # return render(request, 'users/register.html', {'form': form})
    if request.method == "POST":
        form = UserCreationForm(request.Post)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created!')
            return redirect('index')

    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})
