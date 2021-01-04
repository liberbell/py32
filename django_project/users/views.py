from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
    # form = UserCreationForm()
    # return render(request, 'users/register.html', {'form': form})
    if request.method == "POST":
        form = UserCreationForm(request.Post)

    else:
        form = UserCreationForm()