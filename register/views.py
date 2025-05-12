from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # print("Form is valid!")  # ✅ Debug
            login(request, form.save())
            # print("User created:", user.username)  # ✅ Debug
            return redirect('tweet_list')
    else:
        form = UserCreationForm()
    return render(request, 'register/register.html', {'form': form})

def user_login(request):
    if(request.method == "POST"):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            next_url = request.POST.get('next')
            if next_url :
                return redirect(next_url)
            else:
                return redirect('tweet_list')
    else:
        form = AuthenticationForm()
    next_url = request.GET.get('next')
    return render(request, 'register/login.html', {'form' : form, 'next' : next_url})

def user_logout(request):
    if(request.method == "POST"):
        logout(request)
        return redirect('tweet_list')