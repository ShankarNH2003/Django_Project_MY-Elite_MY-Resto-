from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from main.forms import AddToCartForm, LoginForm, UserFormUp, signUpForm
from main.models import User, FoodCategory, FoodItem

def index(request):
    items = FoodCategory.objects.all()
    return render(request, 'index.html', {'items': items})

def category_list(request, category_id):
    category = get_object_or_404(FoodCategory, id=category_id)
    food_items = FoodItem.objects.filter(category=category)
    return render(request, 'food_item_list.html', {'category': category, 'food_items': food_items})

def register(request):
    msg = None
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'User created'
            return redirect('login')
        else:
            msg = 'Form is not valid'
    else:
        form = signUpForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})

def login_view(request):
    form = LoginForm(request.POST)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})

def logout_view(request):
    logout(request)
    return redirect('login')

def manageProfile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    form = UserFormUp(request.POST or None, instance=user)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'manageProfile.html', {'form': form, 'user': user})

def food_item_list(request):
    food_items = FoodItem.objects.filter(available=True)
    return render(request, 'food_item_list.html', {'food_items': food_items})

def menu(request):
    # category = get_object_or_404(FoodCategory, id=id)
    items = FoodCategory.objects.all()  # Fetch all food items
    return render(request, 'menu.html', {'items': items})


def about(request):
    return render(request, 'about.html')